"""Chạy tay một câu thử qua đúng luồng của codebase/agent.py, khi chưa nối model trong máy — dùng cho chấm thử CP2.

1) In prompt:      python eval/hien_thi_tay.py B01
   → in SYSTEM và tin nhắn JSON y như agent.py gửi model. Dán cả hai vào ChatGPT / Claude (cuộc trò chuyện mới).
2) Ra câu hiển thị: python eval/hien_thi_tay.py B01 "<JSON model trả về>"
   → đưa JSON qua guardrails.render_reply, in đúng câu học viên sẽ thấy (hoặc câu chặn khi trích dẫn sai).
Câu mà code tự trả lời (mơ hồ / không tra được đoạn) thì in luôn câu hiển thị, không cần model.
"""
import csv
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "codebase"))

import agent  # noqa: E402
from guardrails import NO_SUPPORT, SYSTEM, render_reply  # noqa: E402
from tools import get_passage, search_lesson  # noqa: E402

with open(os.path.join(ROOT, "eval", "benchmark.csv"), encoding="utf-8-sig") as f:
    bench = {r["id"]: r for r in csv.DictReader(f)}
qid = sys.argv[1]
query = bench[qid]["input"].strip()

if agent._is_too_vague(query):
    print("[code tự trả lời, không gọi model]\n" + agent.answer(query)["output"])
    sys.exit()
passages = search_lesson(query)
if passages:
    top = get_passage(passages[0]["code"])
    passages = ([top] if top else []) + passages[1:]
if not passages:
    print("[code tự trả lời, không gọi model]\n" + agent.answer(query)["output"])
    sys.exit()
sources = [{"code": p["code"], "text": p["text"]} for p in passages]

if len(sys.argv) < 3:
    print("===== HƯỚNG DẪN HỆ THỐNG =====\n" + SYSTEM)
    print("\n===== TIN NHẮN =====\n" + json.dumps({"cau_hoi": query, "doan_bai": sources}, ensure_ascii=False))
else:
    out = render_reply(sys.argv[2].strip().strip("`").removeprefix("json").strip(), sources)
    print(out if out is not None else NO_SUPPORT + "\n[guardrails chặn: JSON sai cấu trúc hoặc trích dẫn không có nguyên văn trong đoạn đã tra]")
