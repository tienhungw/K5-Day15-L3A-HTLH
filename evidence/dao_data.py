"""Đào data pre-class cho lát cắt A1 (trợ giảng dưới video) — nhóm HTLH.

Chạy lại:  python evidence/dao_data.py [thư mục data]
Mặc định đọc data-btc/preclass/ (nguyên file BTC cấp, KHÔNG commit — .gitignore đã chặn data-btc/).
Chỉ dùng thư viện chuẩn. In ra số đã tổng hợp; cách đếm ghi ở evidence/data-mining.md.
"""
import csv
import json
import os
import sys
from collections import defaultdict
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")  # console Windows mặc định không in được tiếng Việt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "data-btc", "preclass")
FOLLOW_UP_SECONDS = 180  # "hỏi tiếp" = câu kế tiếp cùng học viên, cùng video, ≤ 3 phút sau khi trợ giảng trả lời


def read(name):
    with open(os.path.join(DATA, name), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def pct(x, n):
    return "%d/%d (%.1f%%)" % (x, n, 100.0 * x / n) if n else "%d/0" % x


chat = read("chat.csv")
reply = {}  # chat id -> data JSON của sự kiện agent_replied
for r in read("events.csv"):
    if r["type"] == "agent_replied":
        reply[r["ref_id"]] = json.loads(r["data"] or "{}")

# Tập gốc: câu học viên hỏi TRỢ GIẢNG ngay dưới video (không tính chat với bạn học AI, không tính buổi lớp).
ta = [c for c in chat if c["channel"] == "video_question" and c["agent_id"] == "teaching_assistant"]
print("Tập gốc — câu hỏi trợ giảng dưới video:", len(ta), "câu ·", len({c["hv"] for c in ta}), "học viên")

# M1: câu trả lời không trích mốc nào trong bài giảng.
# Mẫu số: chỉ những câu trả lời CÓ ghi trường moc_trich_dan (hệ thống bắt đầu ghi trường này từ một ngày, xem in ra).
logged = [c for c in ta if "moc_trich_dan" in reply.get(c["id"], {})]
no_cite = [c for c in logged if not reply[c["id"]]["moc_trich_dan"]]
days = sorted(c["asked_at"][:10] for c in logged)
print("\nM1 · trả lời KHÔNG trích mốc bài giảng:", pct(len(no_cite), len(logged)),
      "· mẫu số = câu có ghi trường moc_trich_dan, %s → %s (UTC)" % (days[0], days[-1]))
print("M2 · học viên nhận ≥1 câu trả lời không trích mốc:",
      pct(len({c["hv"] for c in no_cite}), len({c["hv"] for c in logged})))

# M3: hệ thống tự đánh dấu thiếu ngữ cảnh bài để trả lời.
miss = [c for c in ta if reply.get(c["id"], {}).get("missing_context") is True]
print("M3 · trợ giảng tự báo thiếu ngữ cảnh (missing_context = True):", pct(len(miss), len(ta)))

# M4: hỏi tiếp cùng video trong ≤ 3 phút sau khi được trả lời.
groups = defaultdict(list)
for c in ta:
    groups[(c["hv"], c["transcript"])].append(c)
follow = {}
for g in groups.values():
    g.sort(key=lambda c: c["asked_at"])
    for a, b in zip(g, g[1:]):
        gap = (datetime.fromisoformat(b["asked_at"]) - datetime.fromisoformat(a["created_at"])).total_seconds()
        follow[a["id"]] = gap <= FOLLOW_UP_SECONDS
fu = lambda cs: sum(follow.get(c["id"], False) for c in cs)
cited = [c for c in logged if reply[c["id"]]["moc_trich_dan"]]
print("M4 · hỏi tiếp cùng video ≤3 phút sau câu trả lời:", pct(fu(ta), len(ta)))
print("     · sau câu CÓ trích mốc:   ", pct(fu(cited), len(cited)))
print("     · sau câu KHÔNG trích mốc:", pct(fu(no_cite), len(no_cite)))
print("     · sau câu thiếu ngữ cảnh: ", pct(fu(miss), len(miss)))

# M5: câu hỏi rất ngắn (tình huống khó "câu quá ngắn, mơ hồ").
for t in (10, 20):
    print("M5 · câu hỏi dưới %d ký tự:" % t, pct(sum(int(c["do_dai_cau_hoi"]) < t for c in ta), len(ta)))

# Ví dụ (mã đã ẩn danh của BTC; không có câu chữ học viên viết).
print("\nVí dụ câu trả lời không trích mốc (5 câu đầu theo thời gian):")
for c in sorted(no_cite, key=lambda c: c["asked_at"])[:5]:
    d = reply[c["id"]]
    print("  %s · %s · hỏi %s ký tự · trả lời %s ký tự · ngu_canh=%s · missing_context=%s · hỏi tiếp ≤3 phút=%s"
          % (c["id"], c["transcript"], c["do_dai_cau_hoi"], c["do_dai_tra_loi"], d.get("ngu_canh"),
             d.get("missing_context"), follow.get(c["id"], False)))
