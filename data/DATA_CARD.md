# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Bài học mẫu có mã đoạn (`data/lessons/d01-ai-llm-foundation.md`)

| | |
|---|---|
| Dùng để làm gì | Nguồn dữ liệu nền cho công cụ `search_lesson` và `get_passage` trong `codebase/tools.py`, phục vụ bản chạy thử và bộ câu thử A1 |
| Từ đâu | Nhóm tự viết lại hoàn toàn bằng tiếng Việt theo chủ đề các `kc_code` của Day01 (`program-day01:ai-llm-foundation` — ngày có nhiều câu hỏi trợ giảng nhất: 333/1.091 câu, phủ nhóm video `d01-r1-v01`, `d01-r1-v02`, `d01-r1-v03`). **Không** chép nguyên transcript hay slide của khoá |
| Xử lý những bước gì | Tách kiến thức thành các đoạn ngắn độc lập (2–4 câu/đoạn), gắn mã định danh cố định dạng `D01-V01-01`..`D01-V03-05` kèm tiêu đề ngắn |
| Số dòng / số đoạn | 18 đoạn (`D01-V01-01` → `D01-V01-08`, `D01-V02-01` → `D01-V02-05`, `D01-V03-01` → `D01-V03-05`) |
| Phiên bản / ngày lấy | `v1` · dựng ngày 27/11/2026 |
| Nhãn | `synthetic` |
| Giới hạn | Mới phủ các khái niệm cốt lõi của Day01 (không chứa số lớp attention cụ thể của model nào, không chứa lịch học/phòng học, không chứa code bài giải mini lab, chưa phủ Day02–Day13). **Data tự dựng không dùng làm bằng chứng pain.** |

**Ghi chú `synthetic`:** Nhóm tự biên soạn thủ công 18 đoạn từ danh sách `kc_code` của Day01 (không sinh hàng loạt); đã kiểm soát toàn bộ 18 đoạn để bảo đảm mã đoạn không trùng và không chứa thông tin ngoài phạm vi bài học.

## Dataset 2 · Nhật ký hành vi pre-class (`data/preclass/` — chỉ dùng số tổng hợp)

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain và lựa chọn các `kc_code` hay sai làm nguồn cho bộ câu thử (`evidence/data-mining.md`, `eval/benchmark.csv`); **không** dùng làm nguồn nội dung trả lời trong bản chạy thử |
| Từ đâu | Dữ liệu BTC cấp cho Track A (`data/preclass/`, 05/11/2026 → 25/11/2026, đã ẩn danh và xáo mã). File gốc giữ cục bộ tại `data-btc/preclass/`, bị `.gitignore` chặn commit |
| Xử lý những bước gì | Lọc bằng script `evidence/dao_data.py` (`channel = video_question`, `agent_id = teaching_assistant`); chỉ lưu số đếm tổng hợp `x/N (%)` và 5 mã lượt chat ẩn danh làm ví dụ |
| Số dòng / số đoạn | Gốc: `chat.csv` 1.260 dòng, `events.csv` 107.709 dòng · Tập lọc A1: 1.091 câu / 144 học viên (mẫu số có ghi `moc_trich_dan` từ 13/11: 557 câu / 84 học viên) |
| Phiên bản / ngày lấy | Bộ phát hành 25/11/2026 (nhóm đào ngày 27/11/2026) |
| Nhãn | thật (đã ẩn danh bởi BTC) |
| Giới hạn | Không có nội dung câu chữ học viên viết (chỉ có độ dài ký tự và metadata), nên không biết nội dung câu hỏi cụ thể chỉ từ data; trường `moc_trich_dan` chỉ bắt đầu ghi từ 13/11/2026 |
