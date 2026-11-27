"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. NHÓM VIẾT phần gọi model thật.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    trả một câu giả cố định, model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Nối OpenAI hoặc DeepInfra: điền MODEL_PROVIDER, MODEL_NAME và API_KEY trong .env,
hoặc cấp các biến môi trường tương ứng. Xem docs/connect-model.md.
"""
import json
import os
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()
CHAT_ENDPOINTS = {
    "openai": ("OpenAI", "https://api.openai.com/v1/chat/completions"),
    "deepinfra": ("DeepInfra", "https://api.deepinfra.com/v1/openai/chat/completions"),
}


def require_live_config() -> None:
    """Kiểm cấu hình gọi thật trước khi gửi câu hỏi."""
    if MODEL_PROVIDER == "fake":
        raise RuntimeError("Đang ở chế độ fake. Điền MODEL_PROVIDER, MODEL_NAME và API_KEY qua .env hoặc biến môi trường.")
    if MODEL_PROVIDER not in CHAT_ENDPOINTS:
        raise NotImplementedError("Nhánh API hỗ trợ MODEL_PROVIDER=openai hoặc deepinfra. Xem docs/connect-model.md.")
    if not MODEL_NAME or not API_KEY:
        raise RuntimeError("Cần điền MODEL_NAME và API_KEY qua .env hoặc biến môi trường.")


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}

    require_live_config()
    provider, endpoint = CHAT_ENDPOINTS[MODEL_PROVIDER]
    messages = [{"role": "system", "content": system}] if system else []
    messages.append({"role": "user", "content": user})
    request = urllib.request.Request(
        endpoint,
        data=json.dumps({"model": MODEL_NAME, "messages": messages}, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.load(response)
    except urllib.error.HTTPError as error:
        error.close()
        raise RuntimeError(f"{provider} HTTP {error.code}") from None
    except (urllib.error.URLError, TimeoutError):
        raise RuntimeError(f"Không kết nối được API {provider} hoặc hết thời gian chờ.") from None
    except ValueError:
        raise RuntimeError(f"API {provider} trả về phản hồi ngoài định dạng JSON.") from None

    try:
        usage = result["usage"]
        tokens_in, tokens_out = usage["prompt_tokens"], usage["completion_tokens"]
        text = result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        raise RuntimeError(f"Phản hồi {provider} thiếu nội dung hoặc usage.") from None
    if text is None:
        text = ""  # Guardrail xử lý trường hợp model không cung cấp nội dung.
    if not isinstance(text, str):
        raise RuntimeError(f"Nội dung phản hồi {provider} phải là chuỗi.")
    return {"text": text, "model": MODEL_NAME, "tokens_in": tokens_in, "tokens_out": tokens_out}
