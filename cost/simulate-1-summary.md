# Tóm tắt mô phỏng simulate-1@20261128-083636

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 23 | 1 | 578 | 55 | 0.7 | 1.6 |
| dung_vua | 19 | 1 | 674 | 66 | 0.8 | 1.6 |
| dung_nhieu | 8 | 1 | 416 | 64 | 0.5 | 1.5 |

Tỉ lệ đạt dùng để tính: 20/21 (95%) — lượt run-2@20261128-083514

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (230 người) | Chi phí / tháng — cơ sở (350 người) | Chi phí / tháng — cao (700 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| deepseek-ai/DeepSeek-V4.1-Flash-1017 (vào 0.2 · ra 0.6 $/1M) | $0.00015 | $0.00016 | $0.00016 | $0.3431 | $0.5221 | $1.04 | $0.0015 |
| zai-org/GLM-5.3 (vào 0.9 · ra 4.0 $/1M) | $0.00077 | $0.00081 | $0.00081 | $1.75 | $2.66 | $5.33 | $0.0076 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: deepseek-ai/DeepSeek-V4.1-Flash-1017. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
