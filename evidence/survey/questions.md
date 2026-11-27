# Khảo sát — hỏi trợ giảng dưới video pre-class

> Nguồn bằng chứng thứ hai, kiểm lại số đào từ data (`evidence/data-mining.md`). Ngưỡng: **≥20 học viên L3 ngoài nhóm HTLH**. Thành viên nhóm không điền.
> Kênh gửi: __ (nhóm lớp / Discord / nhắn riêng) · mở lúc: __ · chốt lúc: __ · link form: __
> Không thu tên, email, mã học viên. Bản xuất lưu ở `results.csv`, đã xoá mọi cột nhận ra người trả lời.

**Tiêu đề form:** Bạn hỏi trợ giảng dưới video pre-class thế nào?

**Mô tả form:** Nhóm HTLH (L3A) đang tìm hiểu cách học viên tự học video pre-class. Khoảng 2 phút, 10 câu, không hỏi tên hay thông tin cá nhân. Hỏi về những lần đã xảy ra, không có câu trả lời đúng sai. Cảm ơn bạn!

## Phần 1 — Bạn là ai

**1. Bạn là:** *(trắc nghiệm, bắt buộc)*
- Học viên L3A
- Học viên L3B
- Khác → *chuyển tới cuối form (Gửi)*

**2. Lần gần nhất bạn xem video pre-class là khi nào?** *(trắc nghiệm, bắt buộc)*
- Hôm nay
- Trong 3 ngày qua
- Trong tuần trước
- Lâu hơn nữa
- Chưa xem bao giờ → *chuyển tới cuối form (Gửi)*

**3. Lần gần nhất đó, bạn xem vào khung giờ nào?** *(trắc nghiệm, bắt buộc)*
- Trước 12:00
- 12:00–18:00
- 18:00–23:00
- Sau 23:00
- Không nhớ

**4. Trong 1 tuần qua, bạn đã hỏi trợ giảng ngay dưới video (hoặc bôi đen slide để hỏi) mấy lần?** *(trắc nghiệm, bắt buộc)*
- 0 lần → *chuyển tới cuối form (Gửi)*
- 1–2 lần
- 3–5 lần
- 6–10 lần
- Hơn 10 lần

## Phần 2 — Lần gần nhất bạn hỏi trợ giảng

**5. Lần gần nhất bạn hỏi trợ giảng dưới video, bạn đã hỏi gì? Gõ lại gần đúng cũng được.** *(trả lời ngắn, không bắt buộc)*

**6. Sau khi nhận câu trả lời lần đó, bạn đã làm gì?** *(hộp kiểm, chọn nhiều, bắt buộc)*
- Dùng luôn câu trả lời, học tiếp
- Tua lại video để tìm chỗ bài nói về ý đó
- Hỏi tiếp trợ giảng
- Hỏi bạn học hoặc hỏi trên Discord
- Hỏi ChatGPT hoặc công cụ khác
- Bỏ qua, chưa hiểu cũng học tiếp
- Mục khác: ___

**7. Lần đó, bạn có biết câu trả lời dựa vào đoạn nào trong bài không?** *(trắc nghiệm, bắt buộc)*
- Có, câu trả lời chỉ rõ mốc thời gian hoặc đoạn trong bài
- Có, mình tự tìm ra đoạn đó
- Không biết
- Không để ý

**8. Lần đó bạn mất thêm bao lâu (sau câu trả lời) mới hiểu xong ý đó?** *(trắc nghiệm, bắt buộc)*
- Không mất thêm
- Dưới 2 phút
- 2–5 phút
- 5–15 phút
- Hơn 15 phút
- Đến giờ vẫn chưa hiểu hẳn

**9. Trong 1 tháng qua, bạn đã mấy lần thấy câu trả lời của trợ giảng không khớp với bài hoặc với điều giảng viên nói trên lớp?** *(trắc nghiệm, bắt buộc)*
- Chưa lần nào
- 1 lần
- 2–3 lần
- Hơn 3 lần
- Không để ý

**10. Nếu có, kể ngắn lần gần nhất đó: bạn hỏi gì, câu trả lời sai hoặc lệch thế nào, bạn phát hiện ra bằng cách nào.** *(đoạn, không bắt buộc)*

## Đếm thế nào (ghi trước khi xem kết quả)

- **Mẫu số:** người chọn L3A hoặc L3B ở câu 1 **và** đã hỏi trợ giảng ≥1 lần ở câu 4.
- **Số chính:**
  - x/N chọn "Tua lại video" hoặc "Hỏi tiếp trợ giảng" ở câu 6.
  - x/N chọn "Không biết" hoặc "Không để ý" ở câu 7.
  - Phân bố số phút ở câu 8, dùng cho cột "mỗi lần tốn gì" ở spec §2.
  - x/N đã từng thấy câu trả lời không khớp ở câu 9.
- Câu 4 cho tần suất / tuần, dùng cho persona ở `cost/personas.yaml`.
- Câu 5 cho câu thử thật trong `eval/benchmark.csv`, cột `source` ghi `nguoi_dung: KS-<số dòng trong results.csv>`.
- Câu 10 cho trích dẫn nguyên văn (≤2 câu mỗi người, bỏ mọi chi tiết nhận ra người viết).
