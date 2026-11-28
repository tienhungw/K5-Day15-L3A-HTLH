# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Viết bộ gate theo checkpoint, kiểm mã đoạn và trích dẫn, thêm nhánh gọi OpenAI. | Codex đã chạy bộ test cục bộ. Hiệp kiểm lại trên bài mẫu và chạy API thật. | Chử Văn Hiệp |
| Prompt / thiết kế lời gọi mô hình | Codex | Viết prompt chọn một trong ba nhánh và trả trích đoạn dưới dạng JSON. | Hiệp và Liêm rà cách chọn đoạn và đầu ra ba nhánh trên bài mẫu. | Chử Văn Hiệp, Nguyễn Thanh Liêm |
| Tích hợp và chuẩn bị mô phỏng (CP3) | Codex | Chạy `eval --try`, đối chiếu token và trích dẫn, điền cấu hình chi phí theo §2 và giá niêm yết DeepInfra. | Codex kiểm CSV, trace và cấu hình cục bộ. Hiệp rà lại trước khi bàn giao. | Chử Văn Hiệp |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code | Viết `evidence/dao_data.py`, đề xuất cách đếm M1–M5 | Chạy lại script, đối chiếu tay __ dòng với `chat.csv` / `events.csv`, khớp __ | Nguyễn Tiến Hưng |
| Sắp khung repo, nháp canvas / TEAMS (CP1) | Claude Code | Chép starter-repo ra thư mục gốc, nháp các dòng canvas | Cả nhóm đọc lại canvas, sửa lời cho đúng ý nhóm | Nguyễn Tiến Hưng |
| Rà câu hỏi phỏng vấn / khảo sát | Claude Code | Soạn 7 câu hỏi mở về chuyện đã xảy ra; gắn nhãn 22 câu trả lời khảo sát (`evidence/survey/nhan.csv`) và viết `dem_khao_sat.py` | Đọc lại 22 dòng nhãn đối chiếu `results.csv`, sửa dòng gắn sai: __ dòng | Nguyễn Tiến Hưng |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Chấm thử 5 output (CP2) | Claude Code | Gợi ý điểm và lý do cho 5 câu, có đối chiếu đoạn bài | Hưng đọc 5 output, đồng ý B01, B06, B10, B11 = 1; B13 = 0 với lý do của mình | Nguyễn Tiến Hưng |
| Giao diện web & tài liệu deploy (CP3) | Antigravity (Gemini) | Viết `codebase/web.py` (HTTP API + rate limit + CORS), `deploy/pages/index.html`, cấu hình Docker và `docs/deploy.md` | Liêm kiểm thử cục bộ các endpoint `/`, `/health`, `/passages`, `/passage`, `/ask` (kể cả chặn vượt 400 ký tự) và triển khai lên VPS. | Nguyễn Thanh Liêm |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
