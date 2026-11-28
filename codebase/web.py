"""Giao diện web và HTTP API tối thiểu cho lát cắt A1 (Trợ giảng pre-class).

Chạy local:
    python codebase/web.py

Chỉ dùng thư viện chuẩn Python (http.server). Bọc answer(text) bằng tracing.begin/end
giống codebase/app.py và cung cấp API JSON cho frontend trên Cloudflare Pages:
    GET  /              Trang hỏi-đáp dự phòng (đọc từ deploy/pages/index.html)
    GET  /health        Kiểm tra trạng thái dịch vụ (không lộ bí mật)
    GET  /passages      Danh sách mã đoạn và tiêu đề bài mẫu trong data/lessons/
    GET  /passage?code= Nguyên văn một đoạn bài qua tools.get_passage(code)
    POST /ask           Nhận {"question": "..."}, kiểm tra độ dài + rate limit theo IP → gọi answer()
"""

from __future__ import annotations

from collections import defaultdict, deque
from datetime import datetime, timezone, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import sys
import threading
import time
import urllib.parse

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

CODEBASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CODEBASE_DIR)
if CODEBASE_DIR not in sys.path:
    sys.path.insert(0, CODEBASE_DIR)

import ai  # noqa: E402  (nạp .env trước khi đọc biến môi trường)
import tracing  # noqa: E402
from agent import answer  # noqa: E402
from tools import _load_passages, get_passage  # noqa: E402

HOST = (os.environ.get("WEB_HOST") or "0.0.0.0").strip()
PORT = int(os.environ.get("WEB_PORT") or os.environ.get("PORT") or "8085")
MAX_QUERY_CHARS = int(os.environ.get("MAX_QUERY_CHARS") or "400")
RATE_LIMIT_MAX = int(os.environ.get("RATE_LIMIT_MAX") or "10")
RATE_LIMIT_WINDOW = int(os.environ.get("RATE_LIMIT_WINDOW") or "60")
GLOBAL_DAILY_LIMIT = int(os.environ.get("GLOBAL_DAILY_LIMIT") or "200")
CORS_ORIGIN = (os.environ.get("CORS_ORIGIN") or "*").strip()
FRONTEND_HTML = os.path.join(ROOT_DIR, "deploy", "pages", "index.html")
_VN_TZ = timezone(timedelta(hours=7))


class DailyQuota:
    """Giới hạn tổng số lượt gọi model thật mỗi ngày (giờ VN) trên toàn server."""

    def __init__(self, limit: int) -> None:
        self.limit = max(1, limit)
        self._day = self._today()
        self._count = 0
        self._lock = threading.Lock()

    @staticmethod
    def _today() -> str:
        return datetime.now(_VN_TZ).strftime("%Y-%m-%d")

    def _rollover(self) -> None:
        today = self._today()
        if today != self._day:
            self._day = today
            self._count = 0

    def has_quota(self) -> bool:
        with self._lock:
            self._rollover()
            return self._count < self.limit

    def record(self, model_calls: int) -> None:
        if model_calls <= 0:
            return
        with self._lock:
            self._rollover()
            self._count += model_calls

    def snapshot(self) -> tuple[int, int]:
        with self._lock:
            self._rollover()
            return self._count, self.limit


class RateLimiter:
    """Giới hạn số lượt gọi POST /ask theo IP trong cửa sổ trượt (sliding window)."""

    def __init__(self, limit: int, window_seconds: int) -> None:
        self.limit = max(1, limit)
        self.window = max(1, window_seconds)
        self._hits: dict[str, deque[float]] = defaultdict(deque)
        self._lock = threading.Lock()

    def allow(self, key: str) -> tuple[bool, int]:
        now = time.monotonic()
        cutoff = now - self.window
        with self._lock:
            bucket = self._hits[key]
            while bucket and bucket[0] <= cutoff:
                bucket.popleft()
            if len(bucket) >= self.limit:
                retry_after = max(1, int(bucket[0] + self.window - now) + 1)
                return False, retry_after
            bucket.append(now)
            return True, 0


LIMITER = RateLimiter(RATE_LIMIT_MAX, RATE_LIMIT_WINDOW)
DAILY_QUOTA = DailyQuota(GLOBAL_DAILY_LIMIT)


def _client_ip(headers, fallback_addr: tuple[str, int]) -> str:
    cf_ip = (headers.get("CF-Connecting-IP") or "").strip()
    if cf_ip:
        return cf_ip
    xff = (headers.get("X-Forwarded-For") or "").strip()
    if xff:
        return xff.split(",")[0].strip()
    return fallback_addr[0] if fallback_addr else "unknown"


class TutorHandler(BaseHTTPRequestHandler):
    """Xử lý HTTP request cho trang hỏi-đáp và API của trợ giảng A1."""

    server_version = "HTLHTutorWeb/1.0"

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("[web] %s - %s\n" % (self.address_string(), fmt % args))

    def _send_cors(self) -> None:
        self.send_header("Access-Control-Allow-Origin", CORS_ORIGIN)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Vary", "Origin")

    def _send_json(self, status: int, payload: dict, extra_headers: dict | None = None) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self._send_cors()
        for k, v in (extra_headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, status: int, html_bytes: bytes) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(html_bytes)))
        self.send_header("Cache-Control", "no-store")
        self._send_cors()
        self.end_headers()
        self.wfile.write(html_bytes)

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self._send_cors()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        if path in ("/", "/index.html"):
            if not os.path.exists(FRONTEND_HTML):
                self._send_json(404, {"error": "Không tìm thấy deploy/pages/index.html"})
                return
            with open(FRONTEND_HTML, "rb") as f:
                self._send_html(200, f.read())
            return

        if path == "/health":
            used, limit = DAILY_QUOTA.snapshot()
            self._send_json(
                200,
                {
                    "ok": True,
                    "provider": ai.MODEL_PROVIDER,
                    "model": ai.MODEL_NAME or ("fake" if ai.MODEL_PROVIDER == "fake" else ""),
                    "max_query_chars": MAX_QUERY_CHARS,
                    "rate_limit": f"{RATE_LIMIT_MAX}/{RATE_LIMIT_WINDOW}s",
                    "daily_model_calls": used,
                    "daily_model_limit": limit,
                },
            )
            return

        if path == "/passages":
            items = [{"code": p["code"], "title": p["title"]} for p in _load_passages()]
            self._send_json(200, {"count": len(items), "items": items})
            return

        if path == "/passage":
            qs = urllib.parse.parse_qs(parsed.query)
            code = (qs.get("code") or [""])[0].strip()
            if not code:
                self._send_json(400, {"error": "Thiếu tham số code (ví dụ ?code=D01-V02-04)."})
                return
            passage = get_passage(code)
            if not passage:
                self._send_json(404, {"error": f"Không tìm thấy mã đoạn {code}."})
                return
            self._send_json(200, passage)
            return

        self._send_json(404, {"error": "Đường dẫn không tồn tại."})

    def do_POST(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.rstrip("/")
        if path != "/ask":
            self._send_json(404, {"error": "Đường dẫn không tồn tại."})
            return

        ip = _client_ip(self.headers, self.client_address)
        allowed, retry_after = LIMITER.allow(ip)
        if not allowed:
            self._send_json(
                429,
                {"error": f"Bạn hỏi quá nhanh. Vui lòng thử lại sau {retry_after} giây (giới hạn {RATE_LIMIT_MAX} lượt/{RATE_LIMIT_WINDOW}s)."},
                extra_headers={"Retry-After": str(retry_after)},
            )
            return

        try:
            length = int(self.headers.get("Content-Length") or "0")
        except ValueError:
            length = 0
        if length <= 0 or length > 16384:
            self._send_json(400, {"error": "Nội dung gửi lên không hợp lệ hoặc quá lớn."})
            return

        raw = self.rfile.read(length)
        try:
            body = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send_json(400, {"error": "Dữ liệu phải là JSON hợp lệ."})
            return

        question = (body.get("question") if isinstance(body, dict) else "") or ""
        if not isinstance(question, str):
            self._send_json(400, {"error": "Trường question phải là chuỗi ký tự."})
            return
        question = question.strip()
        if not question:
            self._send_json(400, {"error": "Vui lòng nhập câu hỏi trước khi gửi."})
            return
        if len(question) > MAX_QUERY_CHARS:
            self._send_json(
                400,
                {"error": f"Câu hỏi quá dài ({len(question)}/{MAX_QUERY_CHARS} ký tự). Hãy rút gọn còn một ý hỏi chính."},
            )
            return

        if not DAILY_QUOTA.has_quota():
            self._send_json(
                429,
                {"error": f"Hệ thống demo đã đạt trần {GLOBAL_DAILY_LIMIT} lượt gọi AI trong ngày. Bạn vẫn có thể xem các đoạn bài gốc ở khung bên phải."},
            )
            return

        tracing.begin("app")
        try:
            result = answer(question)
        except Exception as exc:
            tracing.end()
            self._send_json(503, {"error": f"Chưa gọi được mô hình AI: {type(exc).__name__}"})
            return
        summary, _ = tracing.end()
        DAILY_QUOTA.record(summary["model_calls"])

        output = result.get("output", "") if isinstance(result, dict) else str(result)
        self._send_json(
            200,
            {
                "output": output,
                "model": ", ".join(summary["models"]) or "—",
                "model_calls": summary["model_calls"],
                "tool_calls": summary["tool_calls"],
                "tokens_in": summary["tokens_in"],
                "tokens_out": summary["tokens_out"],
            },
        )


def run_server() -> None:
    server = ThreadingHTTPServer((HOST, PORT), TutorHandler)
    print(f"HTLH Tutor Web đang chạy tại http://{HOST}:{PORT} (provider={ai.MODEL_PROVIDER}, max_chars={MAX_QUERY_CHARS}, rate={RATE_LIMIT_MAX}/{RATE_LIMIT_WINDOW}s)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    run_server()
