# Reflection — Chử Văn Hiệp

## 1. Vai trò và phần mình làm

Mình phụ trách nối model, kiểm căn cứ của câu trả lời và chuẩn bị mô phỏng chi phí cho trợ giảng pre-class.\
Trong [`ai.py`](../codebase/ai.py), mình tích hợp DeepInfra và lấy số token từ phản hồi API. [`guardrails.py`](../codebase/guardrails.py) kiểm mã đoạn và đối chiếu trích dẫn với nguyên văn bài.\
Mình điền ba persona, ba kịch bản quy mô và hai mức giá trong [`cost/personas.yaml`](../cost/personas.yaml), rồi chạy thử 10 phiên. Phần cấu hình được đưa lên ở commit `79f6a6a`.\
Mình chạy lượt đánh giá đầu tiên trên 21 câu và bàn giao CSV cùng trace cho Tuyên chấm ở commit `cfa58ad`.

## 2. AI hỗ trợ mình thế nào

Mình dùng Codex để nháp prompt, viết các ca kiểm mã đoạn và hỗ trợ tích hợp lời gọi API.\
Mình dựa vào kết quả gọi DeepInfra và đối chiếu CSV với trace để kiểm tra số token và đầu ra của bản chạy thử.\
Khi nhóm thêm bước lọc đầu vào, một test do Codex viết vẫn giả định lệnh chèn thuần sẽ được gửi tới model.\
Mình cập nhật test để kiểm đúng hai tình huống: lệnh chèn thuần dừng ở bộ lọc, còn câu hỏi học bài đi kèm vẫn được gửi trong phần dữ liệu JSON.

## 3. Một câu thử trượt và điều mình học được

Ở lượt 2, B20 hỏi “Bài hôm nay có khó không?”. Model hỏi lại, trong khi câu trả lời cần nói rõ bài không có thông tin về độ khó.\
Trace cho thấy hai lượt gửi cùng dữ liệu nhưng model chọn hai cách xử lý khác nhau. Mình nhận ra việc để model quyết có thể khiến cả một nhánh đơn giản thiếu ổn định.\
Trên nhánh thử, mình đưa câu hỏi chỉ xin đánh giá độ khó của cả bài sang nhánh báo thiếu thông tin trước khi tra đoạn.\
Mình kiểm hồi quy để bảo đảm câu hỏi về độ khó của một thao tác vẫn được tra bài. Kết quả này mới được kiểm cục bộ. [Báo cáo đánh giá](../eval/report.md) · [PR #11](https://github.com/tienhungw/K5-Day15-L3A-HTLH/pull/11)
