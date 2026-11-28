# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Chấm ở rubric R6.
> Số **không điền tay**: lấy từ `python run.py simulate --rate-from eval/run-2.csv` → `cost/simulate-1-summary.md`.
> Lúc build dùng gói trả theo token của DeepInfra; giá dưới đây là giá niêm yết trả phí.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu theo số câu hỏi trợ giảng mỗi người trong 21 ngày data pre-class (`evidence/dao_data.py` M8, `spec.md` §2), quy về 30 ngày:

  | Persona | Tỉ lệ | Phiên / người / tháng | Lượt hỏi / phiên | Nguồn |
  |---|---:|---:|---:|---|
  | `dung_it` (1–2 câu / 21 ngày) | 38,2% (55/144) | 1,8 | 1 | 71 câu ÷ 55 người × 30/21 |
  | `dung_vua` (3–9 câu) | 38,9% (56/144) | 7,9 | 1 | 311 ÷ 56 × 30/21 |
  | `dung_nhieu` (≥10 câu) | 22,9% (33/144) | 30,7 | 1 | 709 ÷ 33 × 30/21 |

  Mỗi phiên = 1 câu hỏi vì data đếm theo câu hỏi, không có ranh giới phiên. Mỗi lượt lấy ngẫu nhiên một câu trong `eval/benchmark.csv` (loại `thuong`, `kho`).
- **Số người dùng thật** 3 kịch bản (lớp L3 hơn 700 học viên — README hackathon, `spec.md` §2):
  - thấp **230** = 700 × 144/436 (tỉ lệ người có hỏi trợ giảng trong số người có hoạt động, data pre-class)
  - cơ sở **350** = 50% của 700 *(tự ước tính)*
  - cao **700** = toàn bộ lớp *(tự ước tính)*
- **Giá** 2 mức model (USD / 1 triệu token):
  - `deepseek-ai/DeepSeek-V4.1-Flash-1017`: vào 0,20 · ra 0,60 — https://deepinfra.com/deepseek-ai/DeepSeek-V4.1-Flash-1017/api · xem 27/11/2026
  - `zai-org/GLM-5.3`: vào 0,90 · ra 4,00 — https://deepinfra.com/zai-org/GLM-5.3/api · xem 27/11/2026
- **Tỉ lệ đạt** dùng để tính: **20/21 (95%)** — lượt `run-2@20261128-083514` (lượt 2, `eval/run-2.csv`)
- **Đo token trên model** `deepseek-ai/DeepSeek-V4.1-Flash-1017`, **tính giá** cho cả DeepSeek-V4.1-Flash và GLM-5.3. GLM tách token khác nên số token thật có thể lệch *(chưa đo trên GLM ở lượt này)*.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-083636` · **50 phiên** · seed 42 · phiên lỗi 0/50 · trace `traces/simulate-1.jsonl`

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 23 | 1 | 578 | 55 | 0.7 | 1.6 |
| dung_vua | 19 | 1 | 674 | 66 | 0.8 | 1.6 |
| dung_nhieu | 8 | 1 | 416 | 64 | 0.5 | 1.5 |

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (230) | / tháng — cơ sở (350) | / tháng — cao (700) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| DeepSeek-V4.1-Flash (vào 0,2 · ra 0,6 $/1M) | $0.00015 | **$0.00016** | $0.34 | **$0.52** | $1.04 | $0.0015 |
| GLM-5.3 (vào 0,9 · ra 4,0 $/1M) | $0.00077 | $0.00081 | $1.75 | $2.66 | $5.33 | $0.0076 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (95%) — **không coi như đạt 100%**.

**Vì sao rẻ:** mỗi câu chỉ một lời gọi model (workflow cố định, `spec.md` §4), và các nhánh code chặn trước model — câu mơ hồ, câu chỉ trỏ "đoạn này", câu không tra được đoạn nào, câu chỉ có lệnh chèn — **không gọi model**. Trung bình 0,7 lời gọi model / phiên (≈30% câu dừng ở code). Đầu vào chỉ gồm tối đa 3 đoạn bài (~420–680 token), không gửi lại cả bài.

## 3. So với impact

- **Impact / người / tháng** (`spec.md` §2, cơ sở): ≈ **0,75 giờ** học viên đỡ phải đối chiếu / rời bài sang nguồn ngoài (43 giờ / tháng ÷ 58 người nhận câu trả lời không trích mốc). Thấp 11 giờ / tháng, cao 83 giờ / tháng toàn nhóm.
- **Chi phí / người / tháng** (cơ sở, DeepSeek-V4.1-Flash): **$0.0015** — cả lớp 350 người **$0.52 / tháng**; kịch bản cao 700 người với model đắt hơn (GLM-5.3) vẫn chỉ **$5.33 / tháng**.
- **Kết luận một dòng — đáng làm không:** **Đáng làm** — chi phí model không đáng kể so với ≈0,75 giờ / người / tháng (kể cả khi impact thật chỉ bằng kịch bản thấp 11 giờ / tháng, mỗi giờ học viên đỡ được tốn chưa tới $0.05); điểm nghẽn là **chất lượng** (lượt 2 còn trượt B20, model dao động), không phải tiền.

## 4. Độ nhạy và chi phí ngoài model

| Cần gạt | Đổi chi phí / tháng (cơ sở) | Ghi chú |
|---|---|---|
| Đổi DeepSeek-V4.1-Flash → GLM-5.3 | $0.52 → $2.66 (×5,1) | Chỉ đáng nếu GLM giảm lỗi; lượt 2 trên DeepSeek đã 95% |
| Tỉ lệ đạt 95% → 86% (lượt 1) | chi phí / task thành công $0.00016 → ≈$0.00017 | Chất lượng ảnh hưởng chi phí / task thành công ít hơn ảnh hưởng tới niềm tin của học viên |
| Bỏ các nhánh code chặn trước model (mọi câu đều gọi model) | ≈ +40% *(tự ước tính: 0,7 → 1,0 lời gọi / phiên)* | Nhánh code vừa rẻ vừa ổn định hơn model (xem B20 ở `eval/report.md`) |
| Gửi cả bài (18 đoạn) thay vì 3 đoạn tra được | ≈ ×5 token vào *(tự ước tính: bài mẫu ~3.000 token)* | Còn làm loãng ngữ cảnh — đúng ý D01-V03-02 |

- **Chi phí ngoài model:** bản web chạy trên VPS sẵn có của nhóm (`docs/deploy.md`) — chưa tính tiền thuê riêng *(chưa có số)*. Nội dung `data/lessons/` cần người viết và duyệt khi mở rộng sang ngày khác — đây là chi phí lớn nhất khi làm thật *(chưa đo giờ công)*.
- **Quy mô nào còn đáng làm:** chi phí model tăng tuyến tính theo số câu hỏi; ở mọi quy mô lớp học (vài trăm – vài nghìn người) vẫn dưới vài chục USD / tháng. Giới hạn thật là giờ công viết và duyệt bài có mã đoạn.
