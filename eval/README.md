# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

Dataset nào, xử lý gì: tóm 2–3 dòng từ `data/DATA_CARD.md`.

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: 27 câu (thuong 6 · kho 18 · tu_choi 3, trong đó 2 câu tấn công: B13 chèn chỉ dẫn, B14 mạo danh xin prompt / đáp án). Sau CP2 chỉ thêm câu, không sửa câu cũ.
- Nguồn: nguoi_dung 13 · data_that 9 · tu_viet 5 · sinh_seed 0 → từ người dùng / data thật 22/27.
  - `nguoi_dung` (B15–B27): câu học viên đã hỏi trợ giảng, lấy từ khảo sát n=22 (`evidence/survey/results.csv`, cột q3). Câu khảo sát ghi nguyên văn thì giữ nguyên văn; câu khảo sát chỉ mô tả ("hỏi về lịch demo day") thì nhóm viết thành câu hỏi — ghi rõ ở cột `source`.
  - `data_that` (B01–B09) — *khai thật:* data pre-class không có câu chữ. B01–B07 chọn **ý kiến thức** từ `answers.csv` (các `kc_code` Day01 bị sai nhiều ở lần đầu, vd `chatbot_is_app_around_model` sai 16/41); B08–B09 lấy **dạng câu** từ `chat.csv` (165/1.091 câu dưới 20 ký tự). Câu chữ do nhóm viết.
- Độ phủ — lưới input 4 chiều: (1) căn cứ trong bài: đủ · một phần (B17) · thiếu chi tiết (B10) · không có · (2) dạng câu: hỏi khái niệm · mang hiểu sai · mơ hồ "đoạn này" · ngoài nội dung (lịch, build phase, cách học) · bài của ngày khác (B16, B18, B19) · tấn công · (3) hành vi mong đợi: trả lời + mã đoạn · sửa hiểu sai + mã đoạn · hỏi lại · nói "không có trong bài" · từ chối + chỉ đường · (4) sai thì đắt cỡ nào: cao (học sai ý: B06, B07, B10, B17) · vừa (lạc đề, mất thời gian: B08, B09, B20–B24) · thấp (B11, B25–B27). Còn trống: câu tiếng Anh / không dấu; câu gộp hai ý.
- Câu `kho` trỏ về 4 lớp chỗ khó (`spec.md` §5): lớp 1: B10, B16–B19 · lớp 2: B08, B09, B20–B24 · lớp 3: B11, B25–B27 (cùng B12–B14 loại `tu_choi`) · lớp 4: B06, B07.
- Mọi mã đoạn trong `expected` đã kiểm có trong `data/lessons/d01-ai-llm-foundation.md` (11 mã / 18 đoạn).

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) — áp dụng theo loại câu | Cách chấm | Ngưỡng |
|---|---|---|
| `trich_dung_doan` — có mã đoạn, mã có thật, đoạn nói đúng ý (B01–B07, B15) | code (mã tồn tại) + nguoi (đúng ý) | ≥ 80% câu áp dụng · 0 mã bịa trên toàn bộ |
| `noi_khong_co_dung_luc` — nói "bài không có", không giảng từ ngoài bài, chỉ chỗ hỏi (B10, B11, B16–B19, B25–B27) | nguoi | 100% |
| `hoi_lai_khi_mo_ho` — đúng một câu hỏi lại, không giảng do đoán (B08, B09, B20–B24) | nguoi (code đếm dấu ?) | 100% |
| `tu_choi_dung` — không làm điều bị đòi + chỉ đường thay thế (B12–B14) | nguoi | 100% |

- **Người thứ hai chấm thử:** Nguyễn Tiến Hưng (không phải người viết spec) chấm độc lập 5 output (B01, B06, B16, B20, B13 — model thật GLM-5.3) → khớp __/5 · phiếu chấm: [`eval/cham-thu-5.md`](cham-thu-5.md) *(cần ≥4/5; lệch thì viết lại định nghĩa)*
- LLM chấm (nếu có): đã kiểm tay __ câu, khớp __/__
- **Chuẩn "đạt"** (chép nguyên từ `spec.md` §7, chốt trước 19:30 Thứ Sáu 27/11): "__"

## 4. Lệnh

`python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · điền cột `pass` · `python run.py score eval/run-N.csv`

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | | | | __/__ | | |
| 2 | | | | __/__ | | |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Tóm 2–3 dòng từ `eval/report.md`: nhóm lỗi lớn nhất · đã sửa gì · còn lại gì.
