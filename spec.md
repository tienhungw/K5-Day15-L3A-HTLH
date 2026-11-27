# AI SPEC — Trợ giảng dưới video trả lời có mã đoạn · Nhóm HTLH · Phòng __ · Zone __

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [x] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: A1 · Tutor cho LMS và trang pre-class (tối ưu một điểm trợ giảng đang làm chưa tốt: trả lời có căn cứ trỏ về đoạn bài)
Data BTC cấp đã dùng (nếu có — không commit nguyên file): `data/preclass` — `chat.csv`, `events.csv` (dòng `agent_replied`); chỉ số tổng hợp ở `evidence/data-mining.md`

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại trên trang pre-class (nguồn: `data/preclass/README.md`, `event_types.csv` của bộ đề, và ảnh chụp từ tài khoản của nhóm ngày 27/11/2026):
  1. Học viên mở bài, xem video bài giảng. Bài chia thành các phần có mốc thời gian (ví dụ Ngày 1 có 5 phần, video 21:51); câu hỏi quiz bật lên giữa video.
  2. Chưa hiểu thì gõ câu hỏi vào khung "Tương tác lớp học → Trao đổi" bên phải video (1.091 câu, 144 học viên, 05–25/11), hoặc bôi đen chữ trên slide rồi bấm hỏi (433 lượt `slide_text_asked`).
  3. Trợ giảng trả lời sau khoảng 2,4 giây (trung vị; p90 4,6 giây). Khi có trích dẫn, câu trả lời kèm các nút "Trong bài giảng ở **Phần 1 · 00:40**" để mở đúng mốc video (ảnh dưới). 231/557 câu trả lời (41,5%) không có mốc nào. Dưới ô nhập có dòng "Câu trả lời được grounding theo nội dung buổi học".
  4. Học viên đọc câu trả lời, rồi hỏi tiếp, tua lại video, hoặc rời trang sang ChatGPT / Gemini / internet hoặc hỏi bạn, lab coach (15/20 người trả lời khảo sát).

  ![Trợ giảng dưới video: câu hỏi "Bài hôm nay có khó không?" và câu trả lời kèm mốc Phần 1 · 00:40, Phần 1 · 01:28](evidence/img/tro-giang-duoi-video.png)

  *Ảnh chụp tài khoản của Nguyễn Tiến Hưng, 27/11/2026. Câu hỏi giống câu KS06 và KS10 kể đã hỏi. Ở lượt này trợ giảng có trích mốc, nhưng mốc 00:40 và 01:28 trỏ vào phần mở đầu, còn ý "năm phần, khoảng hai mươi phút" lấy từ cấu trúc bài: học viên không biết mốc nào đỡ cho câu nào.*
- Công cụ / AI đang được dùng: trợ giảng AI ("Trợ giảng Snoop") trong khung Tương tác lớp học của trang pre-class. Ngữ cảnh nó dùng có hai mức: chỉ đoạn quanh lúc hỏi (`hep`, 91 câu) hoặc lời giảng cả ngày (`ca_ngay`, 458 câu); 542 câu không ghi trường này. Tên model ghi chung là `model_chinh` / `fallback`. Cách chọn mốc trích dẫn bên trong: **chưa kiểm**.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): học viên L3 khoá 5 tự xem video pre-class ngoài giờ lớp (phần lớn ở nhà hoặc phòng trọ, theo khảo sát) và hỏi trợ giảng ngay dưới video khi chưa hiểu một ý.
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI): hiểu đúng một ý trong video bài giảng trước buổi lớp, khi tự học một mình và không có ai bên cạnh để hỏi.
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ:
  - **Giải bằng:** hỏi trợ giảng dưới video (1.091 câu, 144 học viên, 05–25/11). Nghi câu trả lời thì sang ChatGPT, Gemini, internet (12/20) hoặc hỏi bạn, lab coach (3/20).
  - **Hỏng ở đâu:** 41,5% câu trả lời không trỏ về mốc nào trong bài (data). 13/20 người đã gặp câu trả lời lệch bài. Chỉ 7/20 kiểm lại được với bài, trung vị 7,5 phút.
  - **Vì sao chưa bỏ:** "vẫn ưu tiên hỏi trợ giảng vì tiện, ko phải chuyển tab" (KS15); "hiện sẵn và có hướng dẫn hỏi" (KS03).
- Pain (KHÔNG chữ AI): học viên L3 — tự xem video pre-class, hỏi ngay dưới video khi chưa hiểu — câu trả lời không chỉ ra đoạn nào trong bài nói điều đó và có lúc lệch bài — họ không tự kiểm được với bài, mất khoảng 7,5 phút đối chiếu hoặc rời bài sang nguồn ngoài không theo cách giảng của khoá; có người còn "không biết nó sai hay đúng" (KS17).
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`):
  - **Data:** 231/557 câu trả lời (41,5%) không trích mốc bài; 58/84 học viên (69%) gặp ít nhất một lần.
  - **Khảo sát** (n = 22, 20 người từng hỏi trợ giảng): 13/20 từng gặp câu trả lời lệch bài · 15/20 phải sang nguồn khác · 7/20 kiểm lại với bài (trung vị 7,5 phút).
  - **Kết luận:** giả thuyết **đúng một phần**; giữ lát cắt, hậu quả chỉnh thành "rời bài sang nguồn ngoài".

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| A · Trả lời kèm mã đoạn của bài; nói "không có trong bài" khi không có căn cứ; hỏi lại khi câu hỏi chỉ trỏ "đoạn này" | 58/84 học viên có hỏi (69%) nhận ≥1 câu không trích mốc *(data)* · 13/20 người khảo sát từng gặp câu trả lời lệch bài | ≈533 câu trả lời không trích mốc / tháng *(data: 231 câu trong 13 ngày × 30/13)* | Trung vị 7,5 phút đối chiếu với bài (3,5–12,5; 7 người), hoặc rời bài sang nguồn ngoài (15/20) | ≈11–83 giờ học viên / tháng, cơ sở ≈43 giờ (công thức dưới) | Kịp: một công cụ tra đoạn + một lời gọi model | **Chọn** |
| B · Chỉ hỏi lại khi câu hỏi quá ngắn / mơ hồ | 165/1.091 câu hỏi (15,1%) dưới 20 ký tự *(data)* · 6/20 câu đã hỏi chỉ trỏ "đoạn này" hoặc quá rộng *(khảo sát)* | ≈236 câu / tháng *(165 trong 21 ngày × 30/21)* | Một câu trả lời lệch ý + một lượt hỏi lại *(chưa đo số phút)* | chưa tính được | Kịp | Gộp vào A thành một nhánh |
| C · Báo cáo "lớp đang kẹt gì" cho giảng viên trước buổi | Giảng viên khoá *(số người: chưa có nguồn)* | 1 lần / buổi *(tự ước tính)* | Thời gian giảng viên tự đoán chỗ kẹt *(chưa có số)* | chưa tính được | Khó: người dùng là giảng viên, khó gặp đủ trong 2 ngày | Không |

- **Impact / tháng** của hướng A = số câu trả lời không trích mốc × tỉ lệ người bị ảnh hưởng × số phút mỗi lần. Chạy `python evidence/survey/dem_khao_sat.py` ra đúng các số này:
  - **Thấp:** 533 × 7/20 (chỉ người kiểm với bài) × 3,5 phút ≈ 653 phút ≈ **11 giờ**
  - **Cơ sở:** 533 × 13/20 (người đã gặp câu trả lời lệch bài) × 7,5 phút (trung vị) ≈ 2.599 phút ≈ **43 giờ**
  - **Cao:** 533 × 15/20 (người phải sang nguồn khác) × 12,5 phút ≈ 4.998 phút ≈ **83 giờ**
  - Nguồn: 533 từ `evidence/dao_data.py` (M1, M9); tỉ lệ và số phút từ `evidence/survey/` (n = 20). *(tự ước tính: lấy tỉ lệ theo người áp cho từng câu trả lời; số phút chỉ có từ 7 người)*
  - Mỗi học viên nhận câu không trích mốc (58 người): cơ sở ≈ 43 giờ ÷ 58 ≈ **0,75 giờ / người / tháng**.
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
  - **C:** bằng chứng phải đến từ giảng viên, nhóm khó hẹn đủ người trước CP3; data pre-class chỉ đo phía học viên.
  - **B** không làm riêng: 6/20 câu mơ hồ được gộp vào A thành nhánh hỏi lại của cùng một quyết định.
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8). Nguồn `evidence/dao_data.py` M8, 144 học viên có hỏi trợ giảng, 21 ngày, quy ra 30 ngày:

  | Kiểu | Tỉ lệ học viên | Câu hỏi / người / tháng | Đối chiếu khảo sát (q5) |
  |---|---|---|---|
  | dùng ít (1–2 câu trong 21 ngày) | 55/144 (38,2%) | ≈1,8 *(71 câu ÷ 55 người × 30/21)* | KS03, KS17: 1 lần |
  | dùng vừa (3–9 câu) | 56/144 (38,9%) | ≈7,9 *(311 ÷ 56 × 30/21)* | KS05: 7 · KS15: 6–7 · KS19: 7–8 · KS09, KS22: 3–4 |
  | dùng nhiều (≥10 câu) | 33/144 (22,9%) | ≈30,7 *(709 ÷ 33 × 30/21)* | KS02: 20 · KS06: 25 · KS13: 26 · KS14: 27 · KS18: 28 |

  Chỉ tính người đã hỏi trợ giảng (144/436 người có hoạt động). Khảo sát hỏi "số lần phải hỏi chỗ khác", không phải số câu hỏi, nên chỉ dùng để đối chiếu thứ bậc. Quy mô thật khi phóng lên (lớp L3 hơn 700 học viên) tính ở §8.

## §3. Giải pháp tương tự *(guide 2.1)*

> Mỗi người thử nhanh 1 sản phẩm, 10 phút. Dòng ghi "chưa kiểm" là chưa có người trong nhóm tự thử: thử xong thì sửa lại đúng điều thấy được.

- **Trợ giảng dưới video hiện tại của trang pre-class** (chính là cách đang làm; data + ảnh §0): đáng học: trả lời nhanh (trung vị 2,4 s) ngay tại chỗ; khi có trích dẫn thì là nút bấm mở đúng mốc video, rất hợp để tự kiểm · đáng né: 41,5% câu trả lời không trích mốc nào; khi có mốc thì mốc gắn cả câu trả lời, không gắn từng ý, nên học viên không biết ý nào lấy từ đâu · mình khác: **mọi** câu trả lời phải trỏ về mã đoạn có thật, không có đoạn căn cứ thì nói "không có trong bài" thay vì trả lời từ trí nhớ model.
- **NotebookLM (Google)**, trả lời dựa trên tài liệu người dùng tải lên, kèm số trích dẫn bấm vào mở đúng đoạn nguồn *(theo mô tả công khai của Google; nhóm **chưa kiểm**, Hưng thử 10 phút với 1 đoạn bài viết lại)*: đáng học: trích dẫn bấm được, người dùng tự kiểm ngay · đáng né: học viên phải tự tải tài liệu lên, rời khỏi video đang xem · mình khác: gắn sẵn vào video đang xem, nguồn là bài của khoá, trỏ về đúng đoạn trong video.
- **ChatGPT / Gemini dùng riêng** (cách học viên đang làm thay: 12/20 người khảo sát sang ChatGPT, Gemini, AI khác hoặc internet khi nghi câu trả lời; KS19: "Sau đấy mình toàn hỏi GPT thẳng luôn"): đáng học: trả lời được mọi câu · đáng né: không biết bài của khoá nói gì, không trỏ về đâu trong video, có thể trả lời lệch với cách giảng của khoá · mình khác: chỉ trả lời từ đoạn bài tra được.

## §4. Thiết kế *(guide 2.2, 3.2)*

**Lát cắt một câu.** Một học viên L3 hỏi một câu dưới video pre-class, trợ giảng chọn trả lời kèm mã đoạn, hỏi lại một câu hoặc báo thiếu căn cứ để học viên biết cách kiểm lại với bài hoặc hỏi tiếp.

**Ngoài phạm vi**

- Làm hộ bài tập hoặc cung cấp lời giải hoàn chỉnh cho bài học viên cần tự làm.
- Tra web hoặc dùng bài khác để trả lời câu hỏi về video đang xem.
- Gửi tin cho TA, chấm điểm hoặc thay đổi dữ liệu của khoá học.

```mermaid
flowchart TD
    Q["Học viên gửi câu hỏi"] --> B{"Câu hỏi quá ngắn hoặc mơ hồ?"}
    B -->|Có| C["Hỏi lại một câu"]
    B -->|Đủ thông tin| R["Tra đoạn Day01 và đối chiếu đoạn đầu theo mã"]
    R -->|Có đoạn| M["Model chọn nhánh từ câu hỏi và đoạn tra được"]
    R -->|Không tìm thấy đoạn| H["Hiện lời báo và bước tiếp phù hợp"]
    M -->|Mơ hồ| C
    M -->|Thiếu căn cứ hoặc ngoài phạm vi| H["Hiện lời báo và bước tiếp phù hợp"]
    M -->|Có căn cứ| V{"Mã đoạn và trích dẫn hợp lệ?"}
    M -->|Sai định dạng| F["Báo chưa đủ căn cứ và chỉ đường hỏi TA"]
    V -->|Có| A["Hiện trích đoạn nguyên văn kèm mã"]
    V -->|Thiếu hoặc sai| F
    C -->|Học viên bổ sung câu hỏi| Q
```

**Hình dạng đã chọn · workflow cố định**

- Mỗi câu hỏi có một nguồn tra cứu, một lần chọn nhánh và một bước kiểm trước khi hiện kết quả.
- Vòng lặp để agent tự chọn công cụ sẽ thêm lượt gọi. Chuỗi bước cố định giúp nhóm tái hiện lỗi theo trace và đo chi phí theo từng câu.

**Công cụ trong bản chạy thử**

| Công cụ | Input | Output | Tác động ra ngoài? |
|---|---|---|---|
| `search_lesson` trong `codebase/tools.py` | Câu hỏi dạng `str`, tối đa 3 đoạn mặc định | Danh sách đoạn Day01 có `code`, `title`, `text` và `score`, hoặc danh sách rỗng. | Không. Chỉ đọc bài mẫu cục bộ. |
| `get_passage` trong `codebase/tools.py` | Mã đoạn dạng `str` | Đoạn tương ứng có `code`, `title`, `text`, hoặc từ điển rỗng. | Không. Chỉ đọc bài mẫu cục bộ. |

- **Mức tự động.** AI tự trả lời khi có căn cứ, hỏi lại khi thiếu thông tin và chỉ đường hỏi TA khi chưa có căn cứ. Học viên có thể dùng mã để kiểm lại ngay. Trích sai hoặc bịa nguồn có thể làm học viên học sai ý trước buổi lớp.
- **Chỗ chặn rủi ro.** Prompt coi câu hỏi và đoạn bài là dữ liệu, giới hạn căn cứ ở các đoạn vừa tra và từ chối làm hộ bài. Trước khi hiện câu trả lời, `codebase/guardrails.py` kiểm từng mã đoạn và đối chiếu từng trích dẫn với đoạn tương ứng. Phản hồi sai định dạng hoặc có một trích dẫn không hợp lệ sẽ chuyển sang lời báo thiếu căn cứ và hướng dẫn hỏi TA.
- **Chỗ người duyệt.** Học viên tự kiểm trích dẫn trong bài hoặc hỏi TA để được giải thích. TA hoặc giảng viên xem xét và thực hiện các việc có tác động như gửi tin, sửa dữ liệu và chấm điểm.

| Nguyên tắc | Chỗ áp dụng |
|---|---|
| G10 · Thu hẹp phạm vi khi không chắc | Hỏi lại một câu khi mơ hồ và dừng ở hướng dẫn hỏi TA khi thiếu căn cứ. |
| Cho người dùng kiểm nguồn | Hiện trích đoạn nguyên văn kèm mã đoạn để học viên đối chiếu. |
| Để người dùng sửa đầu vào | Học viên bổ sung thuật ngữ hoặc gửi lại câu hỏi, rồi workflow tra cứu theo câu mới. |
| Giữ quyền quyết định ở người có thẩm quyền | Công cụ chỉ đọc. TA hoặc giảng viên xử lý các việc ảnh hưởng đến người học hay dữ liệu khoá học. |

**Trạng thái bản chạy.** Công cụ tra cứu đọc bài mẫu Day01 gồm 18 đoạn. DeepInfra đã gọi thật và đo được 51 token vào, 11 token ra trong lần thử kết nối. Chế độ `fake` hiển thị mã đoạn tra được để kiểm luồng cục bộ.

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm

| Tình huống | Học viên thấy gì và làm gì tiếp |
|---|---|
| Suôn sẻ | Nhận trích đoạn nguyên văn kèm mã. Dùng mã để tìm đoạn tương ứng và đối chiếu với video. |
| Không chắc hoặc câu hỏi mơ hồ · lớp 2 | Trợ giảng hỏi một câu để xác định ý hoặc thuật ngữ. Học viên bổ sung chi tiết rồi gửi lại. |
| Thiếu căn cứ · lớp 1 | Với câu ngoài bài, trợ giảng báo không có trong bài và chỉ đường hỏi TA. Với phản hồi có nguồn không khớp, trợ giảng báo chưa đủ căn cứ và đưa cùng hướng dẫn. |
| Người dùng sửa | Học viên gửi lại câu hỏi với thuật ngữ hoặc ngữ cảnh đã sửa. Workflow tra đoạn và quyết định lại theo câu mới. |
| Bị đòi ngoài phạm vi · lớp 3 | Khi bị yêu cầu làm hộ bài tập, trợ giảng nói bài cần tự làm và mời học viên chọn một khái niệm trong video để được giải thích. |
| Trường hợp đặc thù lĩnh vực · lớp 4 | Nếu đoạn bài chứa điều kiện hoặc phủ định, câu trả lời cần giữ phần đó trong trích đoạn để học viên kiểm lại trước buổi lớp. |

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
- Dữ liệu đưa vào model và trace gồm đoạn bài mẫu và câu hỏi đã bỏ thông tin nhận diện. Khóa API dùng cấu hình cục bộ.
- AI chỉ tra và trả lời theo bài, hỏi lại hoặc chỉ đường đến TA. Việc gửi tin, thay đổi dữ liệu hay chấm điểm do người có thẩm quyền thực hiện.
- Học viên có thể hiểu sai trước buổi lớp. Phần hiển thị gắn trích đoạn nguyên văn với mã để học viên mở bài đối chiếu.

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
