"""Đếm kết quả khảo sát (Google Form, câu hỏi mở) — nhóm HTLH.

Chạy:  python evidence/survey/dem_khao_sat.py            (cả 22 dòng)
       python evidence/survey/dem_khao_sat.py --bo KS10,KS11   (bỏ một số dòng để xem số có đổi không)

Đầu vào: nhan.csv — nhãn gắn tay cho từng câu trả lời trong results.csv (định nghĩa nhãn ở questions.md).
Chỉ dùng thư viện chuẩn.
"""
import csv
import os
import statistics
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
# Từ evidence/dao_data.py (M1, M9): 231 câu trả lời không trích mốc trong 13 ngày, quy ra 30 ngày.
NO_CITE_PER_MONTH = 231 * 30 / 13
LEARNERS_NO_CITE = 58  # học viên nhận ≥1 câu không trích mốc (M2)

drop = set()
if "--bo" in sys.argv:
    drop = set(sys.argv[sys.argv.index("--bo") + 1].split(","))

with open(os.path.join(HERE, "nhan.csv"), encoding="utf-8") as f:
    rows = [r for r in csv.DictReader(f) if r["id"] not in drop]


def frac(x, n):
    return "%d/%d (%.0f%%)" % (x, n, 100.0 * x / n) if n else "%d/0" % x


print("Số người trả lời:", len(rows), "(bỏ: %s)" % ", ".join(sorted(drop)) if drop else "")
ask = [r for r in rows if r["hoi_tro_giang"] == "co"]
n = len(ask)
print("Đã từng hỏi trợ giảng dưới video:", frac(n, len(rows)), "→ mẫu số cho mọi số dưới đây")

print("\nLoại câu đã hỏi trợ giảng (q3):")
for k, ten in (("cu_the", "nội dung bài, nêu rõ ý"), ("mo_ho", "nội dung bài nhưng mơ hồ / chỉ \"đoạn này\""),
               ("ngoai_noi_dung", "ngoài nội dung bài (độ khó, lịch, build phase…)"), ("khong_ro", "không nhớ / không nêu")):
    print("  %-15s %-48s %s" % (k, ten, frac(sum(r["loai_cau_hoi"] == k for r in ask), n)))

print("\nq6 · từng thấy câu trả lời không khớp / lệch bài:")
for k in ("co", "khong", "khong_ro"):
    print("  %-9s %s" % (k, frac(sum(r["thay_lech"] == k for r in ask), n)))

chk = [r for r in ask if r["kiem_voi_bai"] == "co"]
mins = [float(r["phut_kiem"]) for r in chk if r["phut_kiem"]]
print("\nq4 · kiểm lại câu trả lời với chính bài (video / slide / tài liệu buổi học):", frac(len(chk), n))
print("     số phút (lấy giữa khoảng): trung vị %.1f · thấp nhất %.1f · cao nhất %.1f (n = %d)"
      % (statistics.median(mins), min(mins), max(mins), len(mins)))

out = [r for r in ask if r["sang_nguon_khac"] == "co"]
print("\nq4–q7 · sau câu trả lời phải sang nguồn khác:", frac(len(out), n))
for k, ten in (("ai_internet", "ChatGPT / Gemini / AI khác / internet"), ("nguoi", "bạn, team, lab coach")):
    print("     %-40s %s" % (ten, frac(sum(r["loai_nguon_khac"] == k for r in out), n)))

times = [float(r["so_lan_thang"]) for r in ask if r["so_lan_thang"]]
print("\nq5 · số lần / tháng (người có ghi số): trung vị %.1f · %s người ghi số"
      % (statistics.median(times), len(times)))

lech = sum(r["thay_lech"] == "co" for r in ask)
med = statistics.median(mins)
low = NO_CITE_PER_MONTH * len(chk) / n * min(mins)
base = NO_CITE_PER_MONTH * lech / n * med
high = NO_CITE_PER_MONTH * len(out) / n * max(mins)
print("\nImpact / tháng = %.0f câu không trích mốc × tỉ lệ × phút (tự ước tính: tỉ lệ theo người áp cho từng câu)" % NO_CITE_PER_MONTH)
print("  thấp    × %d/%d kiểm với bài     × %.1f phút = %.0f phút ≈ %.0f giờ" % (len(chk), n, min(mins), low, low / 60))
print("  cơ sở   × %d/%d thấy lệch bài    × %.1f phút = %.0f phút ≈ %.0f giờ" % (lech, n, med, base, base / 60))
print("  cao     × %d/%d sang nguồn khác  × %.1f phút = %.0f phút ≈ %.0f giờ" % (len(out), n, max(mins), high, high / 60))
print("  cơ sở / học viên gặp câu không trích mốc: %.0f giờ ÷ %d ≈ %.2f giờ / người / tháng"
      % (base / 60, LEARNERS_NO_CITE, base / 60 / LEARNERS_NO_CITE))
