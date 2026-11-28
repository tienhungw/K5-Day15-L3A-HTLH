# Reflection — Nguyễn Thanh Liêm

> Làm ở guide bước 5.3. Mỗi người một file: chép file này thành `reflection/<ten-khong-dau>.md` (viết thường, không dấu). Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. Vai trò + phần mình làm (trỏ tới file / commit):
- Phụ trách dữ liệu bài mẫu, khung tra cứu và toàn bộ phần giao diện web + triển khai demo công khai cho nhóm.
- CP2: soạn 18 đoạn bài mẫu Day01 (`data/lessons/d01-ai-llm-foundation.md`), `data/DATA_CARD.md`, công cụ `codebase/tools.py` và khung `codebase/agent.py` (commit `b409150`).
- CP3: viết HTTP server `codebase/web.py`, giao diện hỏi–đáp bấm mã đoạn mở nguyên văn (`deploy/pages/index.html`), cấu hình Docker (`deploy/Dockerfile`, `deploy/compose.yaml`), `docs/deploy.md` và deploy lên `https://hackathon-htlh.943269.xyz/` (commits `280f375`, `b65e358`, `54b8986`).
- CP4: thêm `MODEL_TEMPERATURE=0` (`codebase/ai.py`), nhánh chặn làm hộ/ngoài phạm vi (`codebase/agent.py`), trần ngày `GLOBAL_DAILY_LIMIT` (`codebase/web.py`), tô sáng câu trích trên web và khung `validation/log.md` (`0ee70f2`), cùng giá cached `$0.006/1M` và quy đổi VNĐ (`74ed330`).

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
- Dùng **Antigravity (Gemini)** để dựng khung `codebase/web.py`, giao diện `deploy/pages/index.html`, cấu hình Docker, `docs/deploy.md`, bổ sung `MODEL_TEMPERATURE=0`, nhánh chặn biên và bảng quy đổi VNĐ; phối hợp rà prompt JSON 3 nhánh với **Codex** cùng Hiệp (`docs/ai-usage.md`).
- Phải tự kiểm tra và sửa lại nhiều chi tiết sau output của AI: đổi endpoint/tài liệu về đúng subdomain `hackathon-htlh.943269.xyz` (`b65e358`), thêm giới hạn an toàn cho link công khai (trần 200 lượt/ngày, 10 lượt/phút/IP, 400 ký tự) để tránh đốt API key khi demo.
- Ngoài ra phải tự test lại cả 21 câu thử trên bản web sau khi chỉnh `agent.py` và đối chiếu kỹ `cost/cost-estimate.md` để tách bạch phần quy đổi VNĐ/cache với số USD đo được từ `simulate-1.csv`, đồng thời giữ nguyên kết quả `run-2` của R5.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
- Nhóm bị trượt `B20` (*"Bài hôm nay có khó không?"*) ở lượt 2 (`run-2@20261128-083514`) khiến điều (3) chỉ đạt `5/6` dù lượt 1 câu này đã qua (`noi_khong_co_dung_luc`).
- So trace hai lượt thấy đầu vào gửi model giống hệt nhau, nhưng model dao động tự đổi từ nhánh báo "không có trong bài" sang "hỏi lại".
- Bài học rút ra là không được giao việc phân loại ranh giới (hỏi độ khó, lịch học, xin tài liệu ngoài, hay từ chối làm hộ như `B12`) cho xác suất của LLM; những nhánh chắc chắn phải đưa về `code` xử lý trước kết hợp đặt `temperature = 0` khi gọi model.
