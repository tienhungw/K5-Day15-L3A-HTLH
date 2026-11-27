# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> **Bản CP2 (27/11):** đào data + 6 câu trả lời viết qua Google Form (P1–P6).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ x/N, script chạy lại được, 5 ví dụ | `evidence/data-mining.md` · `evidence/dao_data.py` |
| Hỏi người dùng: 6 người, câu hỏi mở về chuyện đã xảy ra, **trả lời viết qua Google Form**, mỗi người 1 file | ☑ 6 người, mỗi người 1 file. *Giới hạn:* không có hỏi thêm; cần xác nhận cả 6 là học viên L3 ngoài nhóm | `evidence/interviews/P1.md` … `P6.md` · câu hỏi `KICH-BAN.md` |
| Khảo sát ≥20 người | ☐ bộ câu hỏi đóng đã soạn, chưa gửi | `evidence/survey/questions.md` |

## 2. Số chính

**Đào data** (`data/preclass`, 05–25/11/2026):
- 231/557 câu trả lời của trợ giảng dưới video (41,5%) không trích mốc nào trong bài; 58/84 học viên (69,0%) gặp ít nhất một lần.
- 99/1.091 câu (9,1%) trợ giảng tự báo thiếu ngữ cảnh; sau các câu này 51/99 (51,5%) học viên hỏi tiếp cùng video ≤3 phút, so với 43,5% chung.
- 165/1.091 câu hỏi (15,1%) dưới 20 ký tự.

**Hỏi người dùng** (n = 6, ghi "x/6", không ghi %):
- **5/6** từng thấy câu trả lời của trợ giảng không khớp hoặc "đi hơi xa" với bài (P1, P3, P4, P5, P6). Cả 5 người sau đó đều sang nguồn khác: ChatGPT, Gemini, internet, hỏi bạn.
- **2/6** kiểm lại câu trả lời với chính bài giảng (P3, P4), mất **5–10 phút** và **5–15 phút**.
- **4/6** không kiểm câu trả lời với bài (P1, P2, P5, P6).
- **4/6** câu đã hỏi trợ giảng chỉ trỏ "đoạn này / phần này" hoặc rất chung, không nói rõ ý nào (P3, P4, P5, P6).
- **2/6** câu đã hỏi nằm ngoài nội dung bài: độ khó của bài (P1), xin video khác (P5).
- Số lần / tháng phải tua lại hoặc hỏi chỗ khác sau khi hỏi trợ giảng: P1 25 · P2 1 · P4 khoảng 7 · P5 20 · P3 "mỗi bài … hơn chục lần" · P6 không nêu số.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | học viên khoá 5 *(xác nhận L3)* | Có | 25 | không nêu | slide LMS, ChatGPT, tìm trên mạng |
| P2 | học viên khoá 5 *(xác nhận L3)* | Không | 1 | không nêu | Gemini, câu hỏi mẫu trong khung chat |
| P3 | học viên khoá 5 *(xác nhận L3)* | Có | "mỗi bài hơn chục lần" | 5–10 phút | đối chiếu bài giảng, hỏi bạn, ChatGPT |
| P4 | học viên khoá 5 *(xác nhận L3)* | Có | khoảng 7 | 5–15 phút | xem lại video, internet, ChatGPT, Gemini |
| P5 | học viên khoá 5 *(xác nhận L3)* | Một phần | 20 | không nêu | tìm trên mạng, hỏi bạn nhóm build phase |
| P6 | học viên khoá 5 *(xác nhận L3)* | Một phần | không nêu | không nêu | hỏi AI khác |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "có đôi khi câu trả lời đi hơi xa với bài" — P6
2. "tôi đối chiếu lại với bài giảng , mất khoảng 5- 10p vì để hiểu nữa" — P3
3. "khá nhiều lần, mỗi bài phải phải hơn chục lần, hỏi nhiều nguồn" — P3
4. "Có. Tôi tra cứu thêm trên internet và hỏi chatgpt, gemini" — P4
5. "Tôi đã tự tìm trên mạng, không kiểm lại với bài" — P5
6. "tôi hỏi bạn và hỏi chatgpt , thường là gpt vì khá nhanh có kết quả" — P3
7. "Đọc hiểu. Không kiểm." — P2 *(người không gặp pain)*

Ví dụ từ data (mã đã ẩn danh của BTC): `C00882`, `C00218`, `C00955`, `C00951`, `C01187` (chi tiết ở `evidence/data-mining.md` §4).

## 4. Các nguồn có khớp nhau không

- **Khớp:** data cho thấy 41,5% câu trả lời không trỏ về chỗ nào trong bài. Người dùng kể 5/6 đã gặp câu trả lời lệch bài, và chỉ 2/6 kiểm lại được với bài (mất 5–15 phút). Hai nguồn cùng chỉ một chỗ: câu trả lời khó kiểm với bài.
- **Lệch, và cách giải thích:** trong data, tỉ lệ hỏi tiếp trên trang sau câu có trích mốc và không trích mốc như nhau (43,3% / 42,9%). Người dùng kể rằng khi nghi câu trả lời, họ **rời trang** sang ChatGPT, Gemini, internet, bạn học (5/6). Data pre-class không ghi được việc này, nên chênh lệch không hiện ra trong số hỏi tiếp. Đây là giải thích khả dĩ, chưa đo được.
- **Điều mới, data không cho thấy:** 4/6 câu đã hỏi chỉ trỏ "đoạn này / phần này". Trợ giảng phải biết học viên đang ở đâu trong video, hoặc phải hỏi lại. Điều này khớp với số data: 15,1% câu hỏi dưới 20 ký tự.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đúng một phần, phải chỉnh hậu quả.**
- **Đúng:** học viên không chắc câu trả lời có khớp với bài (5/6) và hiếm khi kiểm được với bài (2/6). Lần kiểm được mất 5–15 phút.
- **Phải đổi:** hậu quả chính không phải "tua lại video" mà là **rời bài sang nguồn ngoài** (ChatGPT, Gemini, internet). Các nguồn này không biết bài của khoá dạy gì.
- **Ngược:** 1/6 (P2) chưa từng thấy câu trả lời lệch và không cần kiểm.
- **Quyết định theo quy tắc ghi trước** ("giữ nếu ≥ một nửa số người kể được lần không chắc câu trả lời"): 5/6, nên **giữ lát cắt** trả lời kèm mã đoạn / "không có trong bài". Thêm vào lát cắt: **hỏi lại một câu khi câu hỏi chỉ trỏ "đoạn này" mà không rõ ý nào**.

**Điều vẫn chưa biết:**
- Cả 6 có đúng là học viên L3 ngoài nhóm không (cần xác nhận).
- Có mã đoạn thì họ có mở ra kiểm thật không: không hỏi được bằng form, kiểm ở bước người dùng thử (guide 4.3).
- Số phút mỗi lần mới có từ 2 người.

## Câu người dùng đã hỏi, dùng cho bộ câu thử (bàn giao Tuyên)

Nguyên văn từ câu 3 của form. Cột `source` ghi `nguoi_dung: P_`. Cột `type` và hành vi mong muốn dưới đây là **đề xuất**, Tuyên chốt khi viết `eval/benchmark.csv`.

| Nguồn | Câu (nguyên văn) | Đề xuất `type` | Hành vi mong muốn (đề xuất) |
|---|---|---|---|
| P3 | đoạn này có thể giải thích kĩ hơn được không | `kho` | Dùng đoạn bài quanh lúc hỏi; nếu không xác định được đoạn thì hỏi lại một câu |
| P4 | Giải thích đoạn này trực quan hơn | `kho` | Giải thích lại kèm mã đoạn; không thêm ý không có trong bài |
| P6 | tôi hỏi về một số vấn đề chưa hiểu | `kho` | Quá mơ hồ: hỏi lại một câu xem chưa hiểu ý nào, không đoán |
| P1 | Tôi hỏi về độ khó của bài hôm đó | `kho` | Không có trong bài: nói rõ là bài không nói về độ khó, không bịa số giờ |
| P5 | Phần này tôi chưa hiểu, có video chi tiết hơn không | `tu_choi` | Không bịa ra video / link không có; nói không có trong bài, chỉ đoạn liên quan hoặc gợi ý hỏi TA |

P2 trả lời "Dùng mẫu có sẵn hỏi", không phải một câu hỏi, nên không dùng làm câu thử. 5 câu từ người dùng đủ ≥1/3 cho bộ 10–15 câu.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Người hỏi | Hình thức · giờ | Đã xong? |
|---|---|---|---|
| học viên khoá 5 (P1–P6) | Nguyễn Tiến Hưng | Google Form, 27/11 | ☑ 6 câu trả lời |
| học viên L3 (hỏi trực tiếp, nếu còn giờ) | Dương Ngọc Tuyên / Nguyễn Thanh Liêm / Chử Văn Hiệp | trực tiếp 5–10 phút, trước CP3 | ☐ (P7+) |
