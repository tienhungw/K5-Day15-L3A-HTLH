"""Workflow trợ giảng pre-class dùng chung cho CLI, eval và mô phỏng."""

import json
import re

from ai import call_model
from guardrails import CLARIFY, HANDOFF, NO_SUPPORT, SYSTEM, render_reply
from tools import _keywords, get_passage, search_lesson
from tracing import note


def _is_too_vague(query: str) -> bool:
    cleaned = re.sub(r"[\W_]+", " ", query).strip()
    return len(cleaned) < 6 or len(cleaned.split()) < 2 or not _keywords(query)


def answer(text: str) -> dict:
    query = (text or "").strip()
    if _is_too_vague(query):
        note("dừng: câu hỏi quá ngắn hoặc mơ hồ")
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
