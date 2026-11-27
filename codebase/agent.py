"""Luồng chính của bản chạy thử — NHÓM VIẾT. Điền ở guide bước 3.2.

`python run.py`, `python run.py eval` và `python run.py simulate` đều gọi answer(text).

Hợp đồng:
    answer(text: str) -> dict có khoá "output" (str): kết quả đưa cho người dùng.
    Token, tên model, số lần gọi model / công cụ: khung tự đếm qua call_model và @tool — không cần trả.
    Bộ chạy gửi NGUYÊN ô input của câu thử vào text. Dữ liệu nền (bài học, thông báo, lịch…)
    do luồng của nhóm tự đọc qua công cụ trong tools.py.

Hình dạng: đúng như sơ đồ ở spec.md §4 (guide bước 2.2) — workflow cố định, một agent, hay nhiều agent.
Công cụ tra cứu hiện vẫn trả dữ liệu mẫu của khung. Phần kiểm phản hồi dùng cùng hợp đồng đoạn bài.
"""
import json

from ai import call_model
from guardrails import CLARIFY, NO_SUPPORT, SYSTEM, render_reply
from tools import search_example
from tracing import note


def answer(text: str) -> dict:
    if not text.strip():
        return {"output": CLARIFY}
    found = search_example(text)
    payload = json.dumps({"cau_hoi": text, "doan_bai": found}, ensure_ascii=False)
    reply = call_model(SYSTEM, payload)
    output = render_reply(reply["text"], found)
    if output is None:
        note("chặn phản hồi: phản hồi sai định dạng hoặc trích dẫn thiếu căn cứ")
        output = NO_SUPPORT
    if reply["model"] == "fake":
        output = "[chế độ giả] " + output
    return {"output": output}
