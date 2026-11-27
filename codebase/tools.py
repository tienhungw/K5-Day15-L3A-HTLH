"""Công cụ của bài toán A1 (Tutor dưới video pre-class) — NHÓM VIẾT.

Mỗi công cụ là một hàm Python có @tool, docstring ghi đủ 4 ý:
    tên · input · output · có tác động ra ngoài không.
Chỉ dùng thư viện chuẩn Python, chỉ đọc dữ liệu mẫu trong data/lessons/.
"""
import os
import re
import unicodedata

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_DIR = os.path.join(ROOT, "data", "lessons")

_STOPWORDS = {
    "la", "gi", "nhu", "the", "nao", "co", "khong", "cua", "va", "trong", "cho",
    "voi", "minh", "ban", "oi", "hay", "giai", "thich", "toi", "biet", "ve",
    "khi", "sao", "tai", "vi", "de", "duoc", "nay", "kia", "do", "thi", "ma",
    "o", "lam", "cach", "bao", "nhieu", "mot", "nhung", "cac", "hoac", "tu",
    "den", "ra", "vao", "len", "xuong", "bai", "video", "em", "anh", "chi",
    "ad", "thay", "hoi", "chut", "a", "nha", "nhe", "vay", "cai", "day",
    "vua", "roi", "luon", "xem", "giup", "chu", "nhi", "ha", "ho", "nua",
    "luc", "nay", "chua", "phai", "khac", "nhau", "cho", "nen", "cang",
}

_HEADER_RE = re.compile(r"^##\s+([A-Za-z0-9_-]+)\s*\|\s*(.+?)\s*$")


def _fold(text: str) -> str:
    """Chuẩn hoá chữ thường, bỏ dấu tiếng Việt để so khớp từ khoá ổn định."""
    s = (text or "").replace("đ", "d").replace("Đ", "d").lower()
    s = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in s if unicodedata.category(ch) != "Mn")


def _keywords(text: str) -> list:
    tokens = re.findall(r"[a-z0-9_]+", _fold(text))
    return [t for t in tokens if len(t) >= 2 and t not in _STOPWORDS]


def _load_passages() -> list:
    """Đọc toàn bộ đoạn bài học có mã đoạn trong data/lessons/*.md."""
    if not os.path.isdir(LESSONS_DIR):
        return []
    passages = []
    for name in sorted(os.listdir(LESSONS_DIR)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(LESSONS_DIR, name)
        current = None
        body = []
        with open(path, encoding="utf-8-sig") as f:
            for raw in f:
                line = raw.rstrip("\r\n")
                m = _HEADER_RE.match(line)
                if m:
                    if current is not None:
                        current["text"] = "\n".join(body).strip()
                        passages.append(current)
                    current = {"code": m.group(1).strip(), "title": m.group(2).strip(), "source_file": name}
                    body = []
                elif current is not None:
                    body.append(line)
        if current is not None:
            current["text"] = "\n".join(body).strip()
            passages.append(current)
    return passages


@tool
def search_lesson(query: str, top_k: int = 3) -> list:
    """search_lesson: Tìm các đoạn bài giảng liên quan nhất tới câu hỏi trong data/lessons/.
    Input: query (str) — câu hỏi hoặc từ khoá cần tra; top_k (int, mặc định 3).
    Output: danh sách dict [{"code", "title", "text", "score"}] sắp theo độ khớp giảm dần; rỗng [] nếu không khớp.
    Tác động ra ngoài: Không (chỉ đọc file mẫu cục bộ)."""
    q_words = _keywords(query)
    if not q_words:
        return []
    passages = _load_passages()
    q_folded = _fold(query)
    scored = []
    for p in passages:
        title_f = _fold(p["title"])
        text_f = _fold(p["text"])
        code_f = _fold(p["code"])
        if code_f in q_folded:
            scored.append((100.0, p))
            continue
        title_tokens = set(re.findall(r"[a-z0-9_]+", title_f))
        text_tokens = set(re.findall(r"[a-z0-9_]+", text_f))
        score = 0.0
        matched = 0
        for w in set(q_words):
            if w in title_tokens:
                score += 3.0
                matched += 1
            elif w in text_tokens:
                score += 1.0
                matched += 1
        min_match = 2 if len(set(q_words)) >= 4 else 1
        if matched >= min_match and score > 0:
            scored.append((score, p))
    scored.sort(key=lambda item: (-item[0], item[1]["code"]))
    return [
        {"code": p["code"], "title": p["title"], "text": p["text"], "score": round(s, 2)}
        for s, p in scored[:max(1, top_k)]
    ]


@tool
def get_passage(code: str) -> dict:
    """get_passage: Lấy đúng một đoạn bài học theo mã đoạn (ví dụ D01-V03-01).
    Input: code (str) — mã đoạn cần đọc.
    Output: dict {"code", "title", "text"} nếu tồn tại, hoặc {} nếu không tìm thấy mã đoạn.
    Tác động ra ngoài: Không (chỉ đọc file mẫu cục bộ)."""
    target = (code or "").strip().upper()
    if not target:
        return {}
    for p in _load_passages():
        if p["code"].upper() == target:
            return {"code": p["code"], "title": p["title"], "text": p["text"]}
    return {}
