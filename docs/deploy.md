# Hướng dẫn chạy & deploy bản web (Nhóm HTLH · Track A1)

> Tài liệu của Nguyễn Thanh Liêm (CP3). Lệnh CLI chính của khung vẫn là `python run.py`.

## 1. Chạy thử trên máy cá nhân (local)

Không cần cài thêm thư viện ngoài (`codebase/web.py` chỉ dùng thư viện chuẩn Python 3.10+).

```bash
python codebase/web.py
```

- Mở trình duyệt tới `http://localhost:8085/` (tự phục vụ `deploy/pages/index.html` và gọi API cùng origin).
- Kiểm tra nhanh sức khoẻ dịch vụ: `GET http://localhost:8085/health`.
- Nếu chưa đặt `.env`, hệ thống chạy chế độ `fake` (`ai.MODEL_PROVIDER = "fake"`).

## 2. Kiến trúc deploy (VPS + Cloudflare)

- **Backend API (`codebase/web.py`):** chạy bằng Docker (`deploy/Dockerfile`, `deploy/compose.yaml`) trên VPS (`ovps`), lắng nghe ở `htlh-tutor:8085`.
- **Reverse Proxy & TLS:** Caddy (`sc01-caddy-1`) trên VPS phục vụ tên miền riêng `https://hackathon-htlh.943269.xyz` (trỏ `reverse_proxy htlh-tutor:8085`), có Cloudflare đứng trước.
- **Frontend tĩnh (`deploy/pages/index.html`):** mở trực tiếp tại `https://hackathon-htlh.943269.xyz/` hoặc deploy thư mục `deploy/pages/` lên Cloudflare Pages (gọi API về `https://hackathon-htlh.943269.xyz`).

### Các endpoint chính
- `GET /health` → trả trạng thái, tên `provider`, `model`, giới hạn ký tự và rate limit (không trả key).
- `GET /passages` → danh sách mã đoạn và tiêu đề trong `data/lessons/`.
- `GET /passage?code=D01-V02-04` → gọi `tools.get_passage(code)` trả nguyên văn đoạn bài để người học tự đối chiếu.
- `POST /ask` → nhận `{"question": "..."}`, bọc `tracing.begin("app")` / `tracing.end()`, gọi `agent.answer(text)`.

## 3. Biến môi trường cần đặt trên host

Đặt trong file `.env` cục bộ trên server (**tuyệt đối không commit lên GitHub**):

| Biến | Bắt buộc | Mặc định | Ý nghĩa |
|---|---|---|---|
| `MODEL_PROVIDER` | Có (khi chạy thật) | `fake` | Nhà cung cấp model (`deepinfra`, `openai`, `anthropic`, `gemini`, `ollama`) |
| `MODEL_NAME` | Có (khi chạy thật) | `""` | Mã model gọi API (CP3 chốt `deepseek-ai/DeepSeek-V4.1-Flash-1017`) |
| `API_KEY` | Có (trừ `ollama`) | `""` | Khoá API của nhà cung cấp |
| `MODEL_URL` | Tuỳ chọn | `""` | URL tương thích OpenAI nếu cần ghi đè |
| `WEB_HOST` / `WEB_PORT` | Không | `0.0.0.0` / `8085` | Địa chỉ và cổng lắng nghe |
| `MAX_QUERY_CHARS` | Không | `400` | Giới hạn số ký tự tối đa mỗi câu hỏi |
| `RATE_LIMIT_MAX` / `RATE_LIMIT_WINDOW` | Không | `10` / `60` | Tối đa 10 lượt `POST /ask` / 60 giây cho mỗi IP |
| `CORS_ORIGIN` | Không | `*` | Nguồn được phép gọi API từ frontend (nên siết về domain Cloudflare Pages khi chốt link) |

## 4. Giới hạn bảo vệ API key đã cài

1. **Giới hạn độ dài đầu vào (`MAX_QUERY_CHARS=400`):** Từ chối HTTP `400` nếu câu hỏi rỗng hoặc vượt quá 400 ký tự.
2. **Rate limit theo IP thật (`10 lượt / 60 giây`):** Đọc `CF-Connecting-IP` (Cloudflare) hoặc `X-Forwarded-For` (Caddy), trả HTTP `429` kèm header `Retry-After` nếu vượt ngưỡng.
3. **Không lộ bí mật & stack trace:** `/health` chỉ trả tên provider/model; lỗi API trả mã `503` chung chung, không in key hay traceback ra response.
4. **Học viên tự kiểm nguồn:** Giao diện tự động chuyển mọi mã `[D01-VXX-YY]` trong câu trả lời thành nút bấm gọi `/passage?code=...`.

## 5. Cập nhật khi `main` có bản sửa mới

Trên VPS trong thư mục repo:

```bash
git pull origin main
docker compose -f deploy/compose.yaml up -d --build
```
