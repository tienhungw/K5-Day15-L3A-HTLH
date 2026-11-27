# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Bản CP1: số đầu tiên, sẽ bổ sung đến CP3.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

## 1. Cách đếm — viết TRƯỚC khi chạy

- **Data dùng:** `data/preclass` BTC cấp (05/11 → 25/11/2026, đã ẩn danh): `chat.csv` (1.260 lượt nhắn) + các dòng `agent_replied` trong `events.csv` (cột `data` có `moc_trich_dan`, `missing_context`, `ngu_canh`). Nguyên file để ở `data-btc/preclass/` trên máy, **không commit**.
- **Tập gốc:** câu học viên hỏi **trợ giảng** ngay **dưới video**: `channel = video_question` và `agent_id = teaching_assistant` → 1.091 câu, 144 học viên. Không tính chat với bạn học AI, không tính câu hỏi trong buổi lớp.
- **Đếm gì:**
  - M1: câu trả lời có `moc_trich_dan` rỗng (không trỏ về mốc nào trong bài giảng).
  - M2: số học viên nhận ≥1 câu như vậy.
  - M3: câu trả lời có `missing_context = True`.
  - M4: câu "hỏi tiếp" = cùng học viên, cùng video (`transcript`), gửi câu kế tiếp ≤180 giây sau khi trợ giảng trả lời câu trước.
  - M5: câu hỏi dưới 10 / 20 ký tự (`do_dai_cau_hoi`).
- **Mẫu số:**
  - M1, M2: chỉ những câu trả lời **có ghi** trường `moc_trich_dan` (hệ thống ghi trường này từ 13/11/2026) → 557 câu, 84 học viên. Câu trước 13/11 không có trường này nên không tính là "không trích".
  - M3, M4, M5: cả 1.091 câu.
- **Script:** [`evidence/dao_data.py`](dao_data.py), chạy `python evidence/dao_data.py` (chỉ thư viện chuẩn). Người khác đặt data BTC vào `data-btc/preclass/` rồi chạy là ra cùng số.

## 2. Đọc trước, đếm sau

Đã đọc `data/preclass/README.md`, `column_dictionary.csv`, `event_types.csv` và các dòng đầu của `chat.csv`, `events.csv`. Các *kiểu* hành vi thấy được:
- Phần lớn lượt nhắn là hỏi trợ giảng dưới video (1.091/1.260); phần còn lại là trò chuyện với bạn học AI.
- Câu trả lời có lúc trích mốc giây trong bài giảng (`moc_trich_dan`), có lúc không; có lúc hệ thống tự đánh dấu thiếu ngữ cảnh.
- Học viên hay hỏi liên tiếp nhiều câu trên cùng một video.
- Có nhiều câu hỏi rất ngắn (vài ký tự). Data không có câu chữ, chỉ có độ dài.
- Câu hỏi dồn về các ngày đầu: Day01 chiếm 333/1.091 câu.

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| M1 · Trả lời không trích mốc nào trong bài | 231 / 557 | 41,5% | 13/11 → 25/11 |
| M2 · Học viên nhận ≥1 câu trả lời không trích mốc | 58 / 84 | 69,0% | cùng giai đoạn |
| M3 · Trợ giảng tự báo thiếu ngữ cảnh | 99 / 1.091 | 9,1% | `missing_context = True` |
| M4 · Hỏi tiếp cùng video ≤3 phút | 475 / 1.091 | 43,5% | tín hiệu chưa rõ nghĩa: có thể là chưa hiểu, có thể là tò mò |
| M4a · … sau câu **có** trích mốc | 141 / 326 | 43,3% | |
| M4b · … sau câu **không** trích mốc | 99 / 231 | 42,9% | **không khác M4a**: data chưa cho thấy thiếu trích mốc làm học viên hỏi lại nhiều hơn |
| M4c · … sau câu thiếu ngữ cảnh | 51 / 99 | 51,5% | cao hơn mức chung ~8 điểm % |
| M5 · Câu hỏi dưới 20 ký tự | 165 / 1.091 | 15,1% | dưới 10 ký tự: 62 (5,7%) |

## 4. ≥5 ví dụ cụ thể (mã đã ẩn danh của BTC, không đoán ai là ai)

Câu trả lời không trích mốc (5 câu đầu theo thời gian hỏi, in từ script):
1. `C01187` · Day06/d06-r1-v01 · hỏi 92 ký tự · trả lời 600 ký tự · ngữ cảnh cả ngày · không hỏi tiếp
2. `C00882` · Day05/d05-r2-v06 · hỏi 18 ký tự · trả lời 220 ký tự · ngữ cảnh hẹp · có hỏi tiếp ≤3 phút
3. `C00218` · Day01/d01-r1-v03 · hỏi 28 ký tự · trả lời 266 ký tự · thiếu ngữ cảnh · có hỏi tiếp
4. `C00955` · Day01/d01-r1-v03 · hỏi 12 ký tự · trả lời 227 ký tự · thiếu ngữ cảnh · có hỏi tiếp
5. `C00951` · Day01/d01-r1-v03 · hỏi 25 ký tự · trả lời 299 ký tự · thiếu ngữ cảnh · có hỏi tiếp

## 5. Giới hạn của data

- Data cho biết trợ giảng **có** trích mốc hay không, **không** cho biết câu trả lời đúng hay sai với bài, và không cho biết học viên có tin câu trả lời hay không.
- Không có câu chữ, nên không phân biệt được câu hỏi ngoài bài và câu trong bài.
- Trường `moc_trich_dan` chỉ có từ 13/11. 144 học viên đã hỏi trợ giảng trên 436 người có hoạt động, nên đây là nhóm học viên có hỏi, không phải cả lớp.
- "Hỏi tiếp ≤3 phút" là ngưỡng nhóm tự chọn.
- → **Kiểm lại bằng phỏng vấn** ≥3 học viên L3 ngoài nhóm: lần gần nhất hỏi trợ giảng dưới video là khi nào, hỏi gì, câu trả lời có dùng được không, có kiểm lại với bài không, kiểm bằng cách nào, mất bao lâu.
