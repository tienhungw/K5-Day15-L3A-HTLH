# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> **Bản CP2 (27/11):** hai nguồn: đào data pre-class + khảo sát Google Form n = 22.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ x/N, script chạy lại được, 5 ví dụ | `evidence/data-mining.md` · `evidence/dao_data.py` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng, giữ log từng câu trả lời) | ☑ 22 người trả lời, 20 người đã từng hỏi trợ giảng; log nguyên văn + nhãn + script đếm | `evidence/survey/results.csv` · `nhan.csv` · `dem_khao_sat.py` · `questions.md` |
| Phỏng vấn (≥3 người, nói chuyện trực tiếp) | ☐ chưa làm; nên có 1–2 cuộc trước CP3 để hỏi sâu "vì sao" | `evidence/interviews/` |

## 2. Số chính

**Đào data** (`data/preclass`, 05–25/11/2026):
- 231/557 câu trả lời của trợ giảng dưới video (41,5%) không trích mốc nào trong bài; 58/84 học viên (69,0%) gặp ít nhất một lần.
- 99/1.091 câu (9,1%) trợ giảng tự báo thiếu ngữ cảnh; sau các câu này 51/99 (51,5%) học viên hỏi tiếp cùng video ≤3 phút, so với 43,5% chung.
- 165/1.091 câu hỏi (15,1%) dưới 20 ký tự.

**Khảo sát** (`python evidence/survey/dem_khao_sat.py`; mẫu số = 20 người đã từng hỏi trợ giảng):
- **13/20 (65%)** từng thấy câu trả lời không khớp hoặc lệch bài ("đi hơi xa với bài", "giải thích chung chung", "theo kiến thức tổng quát"). 5/20 chưa thấy, 2/20 không biết đúng hay sai.
- **15/20 (75%)** sau câu trả lời phải sang nguồn khác: 12/20 sang ChatGPT / Gemini / AI khác / internet, 3/20 hỏi bạn, team, lab coach.
- **7/20 (35%)** kiểm lại câu trả lời với chính bài (video, slide, tài liệu); mất 3,5–12,5 phút, trung vị 7,5 phút.
- Câu đã hỏi trợ giảng: **7/20 (35%) ngoài nội dung bài** (độ khó, lịch học, lịch demo day, kế hoạch build phase, nên xem lại video mấy lần) · **6/20 (30%) mơ hồ / chỉ "đoạn này"** · 5/20 (25%) nội dung bài, nêu rõ ý · 2/20 không nhớ.
- Số lần / tháng (15 người ghi số): trung vị 15.
- **Kiểm độ vững:** bỏ 5 dòng trả lời ngắn nhất (KS10, KS11, KS13, KS14, KS18), tỉ lệ thấy câu trả lời lệch bài vẫn là 10/15 (67%).

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "có đôi khi câu trả lời đi hơi xa với bài" — KS01
2. "Có hồi học day 7, bot giải thích về retrieval hơi khác flow thầy đang trình bày. Mình hỏi lại kèm context cụ thể thì nó trả lời ổn hơn." — KS15
3. "Có lần hỏi về cái flow trong video mà nó giải thích chung chung về agent chứ ko nói đúng cái flow đấy. Mình phải tự tua lại xem." — KS19
4. "Một số ý bot nói không có trong bài nên mình note riêng chứ không ghi chung." — KS21
5. "Mình muốn biết thông tin lấy từ đâu để còn áp dụng vào bài tập, chứ AI nói nghe hợp lý chưa chắc đã đúng." — KS21
6. "tôi đối chiếu lại với bài giảng , mất khoảng 5- 10p vì để hiểu nữa" — KS04
7. "Chưa để ý, có khi mình còn ko biết nó sai hay đúng =)))" — KS17
8. "Còn kiến thức trong bài thì vẫn ưu tiên hỏi trợ giảng vì tiện, ko phải chuyển tab." — KS15 *(vì sao chưa bỏ trợ giảng)*
9. "phần lớn là đều khớp với bài." — KS08 *(người không gặp pain)*

Ví dụ từ data (mã đã ẩn danh của BTC): `C00882`, `C00218`, `C00955`, `C00951`, `C01187` (chi tiết ở `evidence/data-mining.md` §4).

## 4. Các nguồn có khớp nhau không

- **Khớp:**
  - Data: 41,5% câu trả lời không trỏ về chỗ nào trong bài. Khảo sát: 13/20 đã gặp câu trả lời lệch bài, chỉ 7/20 kiểm lại được với bài (trung vị 7,5 phút).
  - KS21 nói thẳng nhu cầu: "muốn biết thông tin lấy từ đâu".
- **Lệch, và cách giải thích:**
  - Trong data, tỉ lệ hỏi tiếp trên trang sau câu có và không trích mốc như nhau (43,3% / 42,9%). Khảo sát cho thấy khi nghi câu trả lời, 15/20 **rời trang** sang nguồn khác, mà data pre-class không ghi được việc này.
  - Có một ngoại lệ: KS15 hỏi lại trợ giảng "kèm context cụ thể" và được trả lời tốt hơn.
  - Đây là giải thích khả dĩ, chưa đo được.
- **Điều mới, data không cho thấy:**
  - 7/20 câu đã hỏi nằm **ngoài nội dung bài** (lịch học, lịch demo day, độ khó, build phase). Trợ giảng bám bài phải nói "không có trong bài" và chỉ đúng nơi hỏi, thay vì đoán.
  - 6/20 câu chỉ trỏ "đoạn này", khớp với số data: 15,1% câu hỏi dưới 20 ký tự.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đúng một phần, phải chỉnh hậu quả.**
- **Đúng:** học viên không chắc câu trả lời có khớp với bài (13/20), và ít người kiểm được với bài (7/20). Lần kiểm được mất trung vị 7,5 phút.
- **Phải đổi:** hậu quả chính là **rời bài sang nguồn ngoài** (15/20), những nguồn không biết bài của khoá dạy gì, chứ không phải "tua lại video".
- **Ngược:** 5/20 chưa từng thấy câu trả lời lệch bài; 2/20 không biết đúng hay sai (KS17: "ko biết nó sai hay đúng"). Rủi ro này còn khó thấy hơn: học viên không biết mình học sai.
- **Quyết định** theo quy tắc ghi trước ("giữ nếu ≥ một nửa số người kể được lần không chắc câu trả lời"): 13/20 → **giữ lát cắt** trả lời kèm mã đoạn / "không có trong bài" / hỏi lại khi mơ hồ. Bằng chứng mới làm rõ hai nhánh: "không có trong bài" (7/20 câu ngoài nội dung) và hỏi lại (6/20 câu mơ hồ).

**Điều vẫn chưa biết:**
- Có mã đoạn thì học viên có mở ra kiểm thật không. Khảo sát không đo được, kiểm ở bước người dùng thử (guide 4.3).
- "Vì sao" sâu hơn. Câu trả lời viết ngắn, chưa có phỏng vấn để hỏi thêm.

## Câu người dùng đã hỏi, dùng cho bộ câu thử (bàn giao Tuyên)

Nguyên văn câu 3 của khảo sát. Cột `source` ghi `nguoi_dung: KS__`. Cột `type` và hành vi mong muốn là **đề xuất**, Tuyên chốt khi viết `eval/benchmark.csv`.

| Nguồn | Câu (nguyên văn) | Đề xuất `type` | Hành vi mong muốn (đề xuất) |
|---|---|---|---|
| KS22 | Giải thích cơ chế hoạt động của RAG | `thuong` | Trả lời từ đoạn bài, mỗi ý một mã đoạn |
| KS17 | (hỏi) agent loop là gì | `thuong` | Trả lời từ đoạn bài, kèm mã đoạn |
| KS15 | Nếu cùng 1 input mà agent trả ra nhiều output khác nhau thì benchmark kiểu gì, có cần chạy nhiều lần rồi lấy trung bình ko? | `kho` | Trả lời phần bài có nói, kèm mã đoạn; phần bài không nói thì nói rõ là không có trong bài |
| KS19 | làm sao phân biệt lỗi do retrieval với lỗi do LLM generate | `kho` | Chỉ dùng điều bài nói; không liệt kê lý thuyết chung không có căn cứ |
| KS21 | Có những tiêu chí nào để chọn test case cho agent và làm sao biết bộ test hiện tại đã đủ tốt chưa? | `kho` | Tách ý có trong bài (kèm mã) và ý không có trong bài |
| KS04 | đoạn này có thể giải thích kĩ hơn được không | `kho` | Dùng đoạn quanh lúc hỏi; không xác định được thì hỏi lại một câu |
| KS05 | Giải thích đoạn này trực quan hơn | `kho` | Giải thích lại kèm mã đoạn, không thêm ý ngoài bài |
| KS01 | tôi hỏi về một số vấn đề chưa hiểu | `kho` | Quá mơ hồ: hỏi lại một câu, không đoán |
| KS11 | Hỏi về lịch học | `tu_choi` | Không có trong bài: không bịa lịch, chỉ nơi xem lịch chính thức |
| KS18 | Hỏi về lịch demo day | `tu_choi` | Như trên |
| KS06 | Tôi hỏi về độ khó của bài hôm đó | `kho` | Bài không nói về độ khó: nói rõ, không bịa số giờ |
| KS02 | Phần này tôi chưa hiểu, có video chi tiết hơn không | `tu_choi` | Không bịa video / link; chỉ đoạn liên quan hoặc gợi ý hỏi TA |

12 câu từ người dùng, đủ ≥1/3 cho cả bộ 20–30 câu ở CP3.
