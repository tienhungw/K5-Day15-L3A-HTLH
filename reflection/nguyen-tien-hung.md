# Reflection — Nguyễn Tiến Hưng (MSSV 2A202603365)

> Đội #4 HTLH · L3A · Phòng H210 · Zone 2. Làm ở guide bước 5.3.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Mình là đội trưởng, lo phần bằng chứng, chấm thử, rồi tự làm cải tiến và hồ sơ CP4.
   - **CP1–CP2:** viết kịch bản phỏng vấn, khảo sát Google Form n = 22 kèm nhãn và script đếm (`evidence/survey/`, commit `829b052`, `46ab53d`), tổng hợp `evidence/summary.md`, `spec.md` §0–§3 (`bf77374`, `7520ac9`). Làm người thứ hai chấm thử 5 output, khớp 5/5 với Tuyên (`eval/cham-thu-cp2.md`, `fbc8e5f`).
   - **CP3:** README thêm link web, video 30 giây, kết quả lượt 1 (`1a1eada`).
   - **CP4:** cải tiến kiểm đầu vào trong `codebase/agent.py` (`6d105f6`), chạy lượt 2 (20/21) và mô phỏng chi phí 50 phiên, viết `eval/report.md`, `cost/cost-estimate.md`, slide `demo-slides.pdf` (`1a5752c`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Mình dùng Claude Code cho hầu hết phần việc của mình. Nó soạn câu hỏi khảo sát, gắn nhãn câu trả lời, đọc trace lượt 1 để tìm nhóm lỗi, viết code cải tiến, nháp báo cáo, phần chi phí và slide (khai ở `docs/ai-usage.md`).
   Chỗ phải sửa: lúc chấm thử ở CP2, Claude Code thêm một hàng "LLM chấm" vào bảng. Mình bỏ hàng đó (`fbc8e5f`), vì người chấm thứ hai phải là người thật. Điểm lượt 2 do AI chấm nháp, nên mình phải tự đọc lại 21 output.
   Mình cũng bắt nó kiểm offline (không gọi model) để chắc cải tiến chỉ đổi đường đi của B13, B14, B17 rồi mới chạy thật. Nếu chỉ tin lời AI nói "đã sửa" thì không biết nó có làm hỏng câu khác không.
   Bài học: AI làm nhanh, nhưng số liệu và quyết định chấm phải do người kiểm.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   **B20 ("Bài hôm nay có khó không?")** qua ở lượt 1 nhưng trượt ở lượt 2, làm nhóm chưa đạt chuẩn điều (3). Lúc đầu mình tưởng cải tiến của mình làm hỏng nó. Xem trace hai lượt thì thấy model nhận **cùng input**: lượt 1 nó trả "không có trong bài", lượt 2 lại hỏi lại. B07 thì ngược lại, tự qua mà không do mình sửa gì.
   Mình học được hai điều:
   - Chạy mỗi câu một lần thì con số tổng (95%) có lẫn cả dao động của model. Muốn biết cải tiến có thật sự giúp không thì phải so trace và chạy lặp nhiều lần.
   - Việc nào code quyết được (câu hỏi về độ khó, lịch học) thì nên để code quyết, đừng để model phân loại. Đúng vậy, sau đó Liêm đã thêm nhánh chặn bằng code cho loại câu này và đặt `temperature = 0`.
   Mình giữ nguyên kết quả trượt trong báo cáo, không chạy lại để chọn lượt đẹp hơn.
