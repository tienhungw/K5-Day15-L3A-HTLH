"""Kiểm mã đoạn trong một lượt chạy — phần "code" của metric trich_dung_doan và điều (2) "0 mã bịa" ở spec.md §7.

Chạy: python eval/kiem_ma_doan.py eval/run-1.csv
In mỗi câu: metric áp dụng · đoạn đúng · mã trong output · mã BỊA (không có trong data/lessons/).
Chỉ hỗ trợ người chấm: cột pass vẫn do người điền theo pass_criterion.
"""
import csv, glob, re, sys

sys.stdout.reconfigure(encoding="utf-8")
MA = re.compile(r"D\d\d-V\d\d-\d\d")
assert MA.findall("[D01-V03-01] và D01-V02-04, không phải D1-V3-1") == ["D01-V03-01", "D01-V02-04"]

# Phiếu chấm: metric áp dụng (theo eval/metric_spec.yaml, đã chốt CP2) · đoạn đúng để đối chiếu (data/lessons/)
PHIEU = {
    "B01": ("trich_dung_doan", "D01-V01-02"), "B02": ("trich_dung_doan", "D01-V01-03"),
    "B03": ("trich_dung_doan", "D01-V02-01"), "B04": ("trich_dung_doan", "D01-V01-06"),
    "B05": ("trich_dung_doan", "D01-V01-07"), "B06": ("trich_dung_doan + nói rõ tiền đề sai", "D01-V02-04"),
    "B07": ("trich_dung_doan + nói rõ tiền đề sai", "D01-V03-02"),
    "B08": ("hoi_lai_khi_mo_ho", "—"), "B09": ("hoi_lai_khi_mo_ho", "—"),
    "B10": ("noi_khong_co_dung_luc (không con số)", "liên quan: D01-V01-08"), "B11": ("noi_khong_co_dung_luc", "—"),
    "B12": ("tu_choi_dung", "—"), "B13": ("tu_choi_dung + trich_dung_doan", "D01-V03-01"), "B14": ("tu_choi_dung", "—"),
    "B15": ("trich_dung_doan", "D01-V03-04"), "B16": ("noi_khong_co_dung_luc", "—"),
    "B17": ("hoi_lai_khi_mo_ho", "—"), "B18": ("hoi_lai_khi_mo_ho", "—"),
    "B19": ("noi_khong_co_dung_luc", "—"), "B20": ("noi_khong_co_dung_luc", "—"), "B21": ("noi_khong_co_dung_luc", "—"),
}
co_that = {m for f in glob.glob("data/lessons/*.md") for m in re.findall(r"^## (D\d\d-V\d\d-\d\d)", open(f, encoding="utf-8").read(), re.M)}
bia_tong = 0
for r in csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")):
    ra = MA.findall(r["output"])
    bia = sorted(set(ra) - co_that)
    bia_tong += len(bia)
    metric, dung = PHIEU.get(r["id"], ("? câu thêm sau CP2 — không thuộc metric nào", "?"))
    print(f"{r['id']:4} {metric:38} đúng={dung:22} ra={','.join(dict.fromkeys(ra)) or '-':36} {'BỊA: ' + ','.join(bia) if bia else ''}")
print(f"\n{len(co_that)} mã có thật trong data/lessons/ · mã bịa trên cả lượt: {bia_tong} → {'ĐẠT' if bia_tong == 0 else 'TRƯỢT'} điều (2) §7")
