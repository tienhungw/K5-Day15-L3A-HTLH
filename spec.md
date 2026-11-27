# AI SPEC — Trợ giảng dưới video trả lời có mã đoạn · Nhóm HTLH · Phòng __ · Zone __

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [x] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: A1 · Tutor cho LMS và trang pre-class (tối ưu một điểm trợ giảng đang làm chưa tốt: trả lời có căn cứ trỏ về đoạn bài)
Data BTC cấp đã dùng (nếu có — không commit nguyên file): `data/preclass` — `chat.csv`, `events.csv` (dòng `agent_replied`); chỉ số tổng hợp ở `evidence/data-mining.md`

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại trên trang pre-class (nguồn: `data/preclass/README.md`, `event_types.csv` của bộ đề; ảnh chụp từ tài khoản của nhóm: **chưa chụp**, Hưng bổ sung):
  1. Học viên mở bài, xem video bài giảng (có câu hỏi bật lên giữa video).
  2. Chưa hiểu thì gõ câu hỏi ở ô hỏi trợ giảng ngay dưới video (1.091 câu, 144 học viên, 05–25/11), hoặc bôi đen chữ trên slide rồi bấm hỏi (433 lượt `slide_text_asked`).
  3. Trợ giảng trả lời sau khoảng 2,4 giây (trung vị; p90 4,6 giây). Câu trả lời có khi kèm mốc giây trong bài giảng (`moc_trich_dan`), có khi không: 231/557 câu (41,5%) không có mốc nào.
  4. Học viên đọc câu trả lời, rồi hỏi tiếp, tua lại video, hoặc học tiếp. Data không cho biết họ có kiểm lại với bài hay không *(kiểm bằng phỏng vấn)*.
- Công cụ / AI đang được dùng: trợ giảng AI dưới video của trang pre-class. Ngữ cảnh nó dùng có hai mức: chỉ đoạn quanh lúc hỏi (`hep`, 91 câu) hoặc lời giảng cả ngày (`ca_ngay`, 458 câu); 542 câu không ghi trường này. Tên model ghi chung là `model_chinh` / `fallback`. Cách chọn mốc trích dẫn bên trong: **chưa kiểm**.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): học viên L3 khoá 5 đi làm ban ngày, buổi tối tự xem video pre-class và hỏi ngay dưới video khi không hiểu một ý.
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI): hiểu đúng một ý trong video bài giảng trước buổi lớp, khi tự học buổi tối và không có ai bên cạnh để hỏi.
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ: hỏi trợ giảng ngay dưới video (1.091 câu, 144 học viên, 05–25/11), tua lại video, hỏi bạn / Discord, hoặc ChatGPT riêng *(các cách ngoài trợ giảng: sẽ kiểm bằng phỏng vấn)*. Chỗ hỏng: 41,5% câu trả lời không trỏ về mốc nào trong bài, nên không tự kiểm được. Vì sao chưa bỏ: hỏi ngay tại chỗ, có trả lời liền *(giả thuyết, kiểm bằng phỏng vấn)*.
- Pain (KHÔNG chữ AI): học viên L3 — tự xem video pre-class buổi tối, hỏi ngay dưới video — câu trả lời không chỉ ra đoạn nào trong bài nói điều đó — không tự kiểm được, phải tua lại / hỏi tiếp, có thể mang ý sai vào buổi lớp.
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): CP1 — 231/557 câu trả lời (41,5%) không trích mốc bài; 58/84 học viên (69%) gặp ít nhất một lần. Chưa chứng minh được là học viên đau vì điều này: tỉ lệ hỏi tiếp sau câu có / không trích mốc như nhau (43,3% / 42,9%). Kiểm lại bằng phỏng vấn ≥3 học viên trước CP3.

## §2. Impact & quyết định chọn *(guide 1.3)*

> **Bản nháp CP2.** Cột "Mỗi lần tốn gì" chờ số phút từ phỏng vấn P1–P4. Điền xong mới tính được impact và chốt lựa chọn (cập nhật đến CP3).

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| A · Trả lời kèm mã đoạn của bài, hoặc nói "không có trong bài" | 58/84 học viên có hỏi (69%) nhận ≥1 câu không trích mốc *(data, 13–25/11)* | ≈533 câu trả lời không trích mốc / tháng *(231 câu trong 13 ngày × 30/13)* | __ phút tua lại tìm chỗ / hỏi lại *(chờ phỏng vấn)*; rủi ro mang ý sai vào buổi lớp | 533 × __ phút = __ giờ | Kịp: một công cụ tra đoạn + một lời gọi model | **Dự kiến chọn** (chốt sau phỏng vấn) |
| B · Hỏi lại một câu khi câu hỏi quá ngắn / mơ hồ | 165/1.091 câu hỏi (15,1%) dưới 20 ký tự *(data)* | ≈236 câu / tháng *(165 câu trong 21 ngày × 30/21)* | Một câu trả lời lệch ý + một lượt hỏi lại *(chưa đo)* | 236 × __ phút = __ giờ | Kịp | Dự phòng: chọn nếu phỏng vấn bác bỏ A |
| C · Báo cáo "lớp đang kẹt gì" cho giảng viên trước buổi | Giảng viên khoá *(số người: chưa có nguồn)* | 1 lần / buổi *(tự ước tính)* | Thời gian giảng viên tự đoán chỗ kẹt *(chưa có số)* | chưa tính được | Khó: người dùng là giảng viên, khó gặp đủ trong 2 ngày | Không |

- **Impact / tháng** của hướng chọn = __ lượt × __ phút = __ — nguồn: số lượt từ `evidence/data-mining.md` (M1, M9), số phút từ `evidence/interviews/P1–P4` *(chờ)*.
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá): **C**: bằng chứng phải đến từ giảng viên, nhóm khó hẹn đủ người trước CP3; data pre-class chỉ đo được phía học viên. **B** giữ làm dự phòng, và cũng thành câu thử loại `kho` cho hướng A.
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8). Nguồn `evidence/dao_data.py` M8, 144 học viên có hỏi trợ giảng, 21 ngày, quy ra 30 ngày:

  | Kiểu | Tỉ lệ học viên | Câu hỏi / người / tháng |
  |---|---|---|
  | dùng ít (1–2 câu trong 21 ngày) | 55/144 (38,2%) | ≈1,8 *(71 câu ÷ 55 người × 30/21)* |
  | dùng vừa (3–9 câu) | 56/144 (38,9%) | ≈7,9 *(311 ÷ 56 × 30/21)* |
  | dùng nhiều (≥10 câu) | 33/144 (22,9%) | ≈30,7 *(709 ÷ 33 × 30/21)* |

  Chỉ tính người đã hỏi trợ giảng (144/436 người có hoạt động). Quy mô thật khi phóng lên (lớp L3 hơn 700 học viên) tính ở §8.

## §3. Giải pháp tương tự *(guide 2.1)*

> Mỗi người thử nhanh 1 sản phẩm, 10 phút. Dòng ghi "chưa kiểm" là chưa có người trong nhóm tự thử: thử xong thì sửa lại đúng điều thấy được.

- **Trợ giảng dưới video hiện tại của trang pre-class** (chính là cách đang làm, theo data): đáng học: trả lời nhanh (trung vị 2,4 s) ngay tại chỗ, có lúc trích mốc giây trong bài · đáng né: 41,5% câu trả lời không trích mốc nào, học viên không biết câu trả lời dựa vào đâu · mình khác: **mọi** câu trả lời phải trỏ về mã đoạn có thật, không có đoạn căn cứ thì nói "không có trong bài" thay vì trả lời từ trí nhớ model.
- **NotebookLM (Google)**, trả lời dựa trên tài liệu người dùng tải lên, kèm số trích dẫn bấm vào mở đúng đoạn nguồn *(theo mô tả công khai của Google; nhóm **chưa kiểm**, Hưng thử 10 phút với 1 đoạn bài viết lại)*: đáng học: trích dẫn bấm được, người dùng tự kiểm ngay · đáng né: học viên phải tự tải tài liệu lên, rời khỏi video đang xem · mình khác: gắn sẵn vào video đang xem, nguồn là bài của khoá, trỏ về đúng đoạn trong video.
- **ChatGPT dùng riêng** (cách học viên có thể đang làm thay; xác nhận qua phỏng vấn câu 7): đáng học: trả lời được mọi câu · đáng né: không biết bài của khoá nói gì, không trỏ về đâu trong video, có thể trả lời lệch với cách giảng của khoá · mình khác: chỉ trả lời từ đoạn bài tra được.

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả):
- Không làm (≥3 điều):
- **Sơ đồ** (ảnh / Mermaid / draw.io): [chèn ở đây]
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  |  |  |  |  |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — __ câu (thuong __ · kho __ · tu_choi __) · metric: `eval/metric_spec.yaml` (__ metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ __% câu qua, và __"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
