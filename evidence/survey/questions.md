# Khảo sát — hỏi trợ giảng dưới video pre-class (Google Form, câu hỏi mở)

> Nguồn bằng chứng thứ hai, kiểm lại số đào từ data (`evidence/data-mining.md`). Ngưỡng: ≥20 học viên L3 ngoài nhóm HTLH.
> **Kết quả:** 22 người trả lời, 27/11/2026 17:16 → 17:59. Thành viên nhóm không điền.
> Kênh gửi: __ *(Hưng điền: nhóm lớp nào / Discord / nhắn riêng)* · người gửi: Nguyễn Tiến Hưng
> Form không thu tên, email, mã học viên. `results.csv` là bản xuất nguyên văn, chỉ giữ dấu thời gian và 7 câu trả lời, đánh mã KS01–KS22 theo thứ tự gửi.

## Câu hỏi trong form (nguyên văn, đều là câu trả lời mở)

1. Lần gần nhất bạn xem video pre-class là hôm nào? Bạn xem lúc mấy giờ, ở đâu?
2. Lần đó có chỗ nào bạn chưa hiểu không? Lúc đó bạn đã làm gì?
3. Lần gần nhất bạn hỏi trợ giảng ngay dưới video, bạn hỏi gì?
4. Câu trả lời lần đó bạn dùng thế nào? Bạn có kiểm lại với bài không? Kiểm bằng cách nào, mất bao lâu?
5. Trong 1 tháng qua, khoảng bao nhiêu lần bạn hỏi trợ giảng xong vẫn phải tua lại video, hỏi bạn, hỏi Discord hay hỏi ChatGPT?
6. Có lần nào bạn thấy câu trả lời không khớp với bài không? Sau đó chuyện gì xảy ra?
7. Khi không hỏi trợ giảng thì bạn hỏi ở đâu? Vì sao chọn chỗ đó?

*(Bản câu hỏi đóng 10 câu soạn trước đó không được gửi.)*

## Cách gắn nhãn (`nhan.csv`)

Câu trả lời mở nên phải gắn nhãn tay trước khi đếm. **Khai thật:** nhãn được định nghĩa sau khi đã đọc câu trả lời. Mỗi nhãn có định nghĩa dưới đây, cột `ghi_chu` trong `nhan.csv` ghi lý do cho dòng khó, để người khác gắn lại và so.

| Cột | Giá trị | Định nghĩa |
|---|---|---|
| `hoi_tro_giang` | co / khong | Đã từng hỏi trợ giảng dưới video (q3, q4). `khong` → không tính vào mẫu số |
| `loai_cau_hoi` | cu_the | q3 hỏi một ý nội dung bài, nêu rõ ý nào |
| | mo_ho | q3 hỏi nội dung bài nhưng chỉ trỏ "đoạn này / phần này / kết quả đó" hoặc quá rộng ("toàn bộ bài") |
| | ngoai_noi_dung | q3 hỏi điều bài giảng không dạy: độ khó, lịch học, lịch demo, kế hoạch build phase, nên học bao nhiêu |
| | khong_ro | q3 không nêu câu hoặc không nhớ |
| `thay_lech` | co / khong / khong_ro | q6: đã từng thấy câu trả lời không khớp, lệch, "chung chung", "theo kiến thức tổng quát" so với bài. `khong_ro` khi người trả lời nói không biết đúng hay sai |
| `kiem_voi_bai` | co / khong | q4: kiểm câu trả lời bằng chính video, slide hoặc tài liệu buổi học |
| `phut_kiem` | số | q4: số phút kiểm, lấy giữa khoảng (5–10 → 7,5) |
| `sang_nguon_khac` | co / khong | q4, q6, q7 (về lần đã hỏi trợ giảng): sau câu trả lời phải hỏi nguồn khác ngoài trợ giảng và bài |
| `loai_nguon_khac` | ai_internet / nguoi | ChatGPT, Gemini, AI khác, internet / bạn, team, lab coach |
| `so_lan_thang` | số | q5 khi có số; khoảng thì lấy giữa (10–20 → 15); "vô số", "hơn chục lần" để trống |

## Đếm

`python evidence/survey/dem_khao_sat.py`. Mẫu số mọi tỉ lệ = người đã từng hỏi trợ giảng (20/22). Thêm `--bo KS10,KS11` để bỏ thử vài dòng, xem kết luận có đổi không.
