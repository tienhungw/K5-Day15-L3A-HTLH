"""Workflow trợ giảng pre-class dùng chung cho CLI, eval và mô phỏng."""

import json
import re

from ai import call_model
from guardrails import CLARIFY, HANDOFF, HOMEWORK, NO_SUPPORT, REFUSE_OVERRIDE, SYSTEM, render_reply
from tools import _fold, _keywords, get_passage, search_lesson
from tracing import note

# --- Kiểm đầu vào trước khi tra đoạn (cải tiến CP4, xem spec.md §10) -------------------------
# Mọi mẫu dưới đây so trên chữ đã bỏ dấu (_fold). Đây là quy tắc chung theo loại câu,
# không so khớp nguyên văn câu thử nào.

# Từ chỉ trỏ: học viên trỏ vào chỗ đang xem mà không nói tên ý ("đoạn này", "phần đó", "ở đây").
_DEICTIC_RE = re.compile(
    r"\b(doan|phan|cho|khuc|y|cai|muc|slide|cau|bai)\s+(nay|do|kia|tren|vua roi)\b|\bo day\b"
)
# Từ chỉ cách giải thích, không phải tên khái niệm của bài.
_REQUEST_WORDS = {
    "giai", "thich", "truc", "quan", "hon", "ky", "ki", "chi", "tiet", "ro", "cu", "the",
    "de", "hieu", "chua", "vi", "du", "them", "lai", "noi", "gion", "don", "gian", "can",
    "muon", "duoc", "khong", "nhe", "toi", "em", "minh", "giup", "voi", "nua", "lam",
}
# Câu xin tài nguyên ngoài bài (video, link, tài liệu khác): để nhánh "không có trong bài" xử lý.
_OUTSIDE_RESOURCE_RE = re.compile(r"\b(video|link|tai lieu|slide khac|khoa hoc khac|nguon khac)\b")

# Câu chèn lệnh: đòi bỏ quy tắc, đổi nguồn, hoặc lộ hướng dẫn hệ thống.
_OVERRIDE_RES = [
    re.compile(r"\b(bo qua|quen|phot lo|ignore)\b.*\b(huong dan|quy tac|chi dan|yeu cau|instruction)"),
    re.compile(r"\bkien thuc rieng\b"),
    re.compile(r"\bkhong can (trich|dua vao|dung) (bai|nguon|doan)"),
    re.compile(
        r"\b(?:cho (?:(?:minh|toi|em) )?(?:xem|doc|xin)|xin|in(?: ra)?|hien thi|tiet lo|"
        r"cung cap|chia se|gui(?: (?:cho )?(?:minh|toi|em))?|show(?: me)?|send(?: me)?|reveal|print|give me) "
        r"(?:(?:nguyen(?: van)?|toan bo|noi dung|your|the) )*(?:huong dan he thong|system prompt)\b"
        r"|\b(?:huong dan he thong|system prompt) cua (?:ban|tro giang|he thong nay)\b"
        r"|\byour system prompt\b"
    ),
]
_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?;\n])\s+")

# Chỉ bắt câu đánh giá cả bài, kể cả khi câu dùng tên chung "video/buổi học/chương".
# Câu hỏi về độ khó của một thao tác hay khái niệm vẫn được tra theo bài.
_LESSON_SUBJECT = r"(?:bai(?: hoc)?|video|buoi hoc|chuong|khoa hoc)(?: (?:nay|do|kia|hom nay|tiep theo))?"
_LESSON_DIFFICULTY_RE = re.compile(
    rf"(?:{_LESSON_SUBJECT} (?:co )?(?:kho|de)(?: khong| lam khong| den muc nao| the nao)?"
    rf"|(?:do kho|muc do kho) cua {_LESSON_SUBJECT}(?: the nao| ra sao| la bao nhieu)?)"
    r"[\s?.!]*"
)
_HOMEWORK_REQUEST_RE = re.compile(
    r"^(?:(?:hay|vui long) )?(?:lam|giai|viet) ho (?:(?:minh|toi|em) )?"
    r"(?:bai (?:tap|lab|mini lab|kiem tra|nop)|mini lab)\b"
)


def _is_too_vague(query: str) -> bool:
    cleaned = re.sub(r"[\W_]+", " ", query).strip()
    return len(cleaned) < 6 or len(cleaned.split()) < 2 or not _keywords(query)


def _only_points_at_video(query: str) -> bool:
    """Câu chỉ trỏ "đoạn này / phần đó…" mà không còn tên ý nào sau khi bỏ từ chỉ cách giải thích.

    Bản chạy thử không biết học viên đang xem tới đâu trong video, nên câu loại này phải hỏi lại.
    """
    folded = _fold(query)
    if not _DEICTIC_RE.search(folded) or _OUTSIDE_RESOURCE_RE.search(folded):
        return False
    rest = _DEICTIC_RE.sub(" ", folded)
    concept_words = [w for w in _keywords(rest) if w not in _REQUEST_WORDS]
    return not concept_words


def _strip_override(query: str) -> tuple[str, int]:
    """Bỏ các câu chèn lệnh khỏi câu hỏi, giữ phần hỏi thật. Trả (phần còn lại, số câu đã bỏ)."""
    kept, dropped = [], 0
    for sentence in _SENTENCE_SPLIT_RE.split(query):
        folded = " ".join(_fold(sentence).split())
        if any(p.search(folded) for p in _OVERRIDE_RES):
            dropped += 1
        elif sentence.strip():
            kept.append(sentence.strip())
    return " ".join(kept), dropped


def answer(text: str) -> dict:
    query = (text or "").strip()
    if _is_too_vague(query):
        note("dừng: câu hỏi quá ngắn hoặc mơ hồ")
        return {"output": CLARIFY}

    query, dropped = _strip_override(query)
    if dropped:
        note(f"bỏ {dropped} câu chèn lệnh trước khi tra đoạn")
        if not query or _is_too_vague(query):
            note("dừng: câu hỏi chỉ có yêu cầu đổi quy tắc / lộ hướng dẫn")
            return {"output": REFUSE_OVERRIDE}

    folded = " ".join(_fold(query).split())
    if _LESSON_DIFFICULTY_RE.fullmatch(folded):
        note("dừng: câu hỏi đánh giá độ khó của bài")
        return {"output": HANDOFF}

    if _HOMEWORK_REQUEST_RE.search(folded):
        note("dừng: yêu cầu làm hộ bài tập")
        return {"output": HOMEWORK}

    if _only_points_at_video(query):
        note("dừng: câu chỉ trỏ 'đoạn này' mà không nêu ý nào")
        return {"output": CLARIFY}

    passages = search_lesson(query)
    if passages:
        top_passage = get_passage(passages[0]["code"])
        passages = ([top_passage] if top_passage else []) + passages[1:]
    if not passages:
        note("dừng: không tìm thấy đoạn phù hợp")
        return {"output": HANDOFF}

    # Chỉ chuyển mã và nội dung đoạn bài cho model. Dùng chính tập đó để kiểm trích dẫn.
    sources = [{"code": passage["code"], "text": passage["text"]} for passage in passages]
    codes = ", ".join(f"[{source['code']}]" for source in sources)
    note(f"tra được {len(sources)} đoạn: {codes}")
    payload = json.dumps({"cau_hoi": query, "doan_bai": sources}, ensure_ascii=False)
    reply = call_model(SYSTEM, payload)
    if reply["model"] == "fake":
        return {"output": f"[chế độ giả] Đã tra đoạn bài: {codes}."}

    output = render_reply(reply["text"], sources)
    if output is None:
        note("chặn phản hồi: phản hồi sai định dạng hoặc trích dẫn thiếu căn cứ")
        output = NO_SUPPORT
    return {"output": output}
