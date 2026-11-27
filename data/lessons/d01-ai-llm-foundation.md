# Bài học mẫu · Day01 (`program-day01:ai-llm-foundation`)

> **Lưu ý dữ liệu:** Nội dung dưới đây do nhóm HTLH tự viết lại hoàn toàn bằng tiếng Việt để chạy thử bản mẫu cho lát cắt A1, **không** chép nguyên transcript hay slide của khoá học. Các ý kiến thức bám theo các `kc_code` của Day01 (nhóm ngày có nhiều câu hỏi trợ giảng nhất: 333/1.091 câu) và các khái niệm dùng để kiểm thử ở `eval/benchmark.csv`.

## D01-V01-01 | Làn sóng AI hiện đại đến từ dữ liệu, kiến trúc và phần cứng
Sự bùng nổ của AI tạo sinh hiện nay không chỉ nhờ một thuật toán mới mà nhờ ba yếu tố cộng hưởng: khối lượng dữ liệu khổng lồ để huấn luyện, kiến trúc Transformer xử lý ngữ cảnh song song hiệu quả, và năng lực tính toán phần cứng (GPU/TPU) đủ lớn để huấn luyện các mô hình tỉ tham số.

## D01-V01-02 | Chatbot là ứng dụng bọc quanh model, không phải bản thân model
Model ngôn ngữ (LLM) về bản chất chỉ nhận chuỗi chữ đầu vào và sinh ra chuỗi chữ đầu ra trong từng lượt gọi. Chatbot mà người dùng sử dụng thực chất là một ứng dụng phần mềm bọc quanh model, bao gồm giao diện trò chuyện, hướng dẫn hệ thống (system prompt), lịch sử hội thoại và các công cụ tra cứu kèm theo.

## D01-V01-03 | Trí nhớ hội thoại nằm ở ứng dụng chứ model không tự nhớ
Bản thân model không lưu trạng thái hay tự nhớ những gì người dùng vừa hỏi ở các lượt trước. Để tạo cảm giác "nhớ" câu vừa nói, ứng dụng chatbot phải lưu lại lịch sử hội thoại rồi ghép và gửi kèm toàn bộ lịch sử đó lên model trong mỗi lần gọi API mới.

## D01-V01-04 | Token là đơn vị chữ nhỏ nhất mà model xử lý
Model không đọc từng chữ cái hay từng từ nguyên vẹn theo cách của con người mà tách văn bản thành các mảnh gọi là token. Một token có thể là một từ tiếng Anh ngắn, một phần từ dài hoặc một âm tiết/dấu câu; vì vậy văn bản tiếng Việt có dấu thường tốn nhiều token hơn tiếng Anh cùng nội dung.

## D01-V01-05 | Chi phí dùng API tính theo cả token vào và token ra
Mỗi lượt gọi model đều tính phí dựa trên hai phần: số token đầu vào (gồm hướng dẫn hệ thống, tài liệu đính kèm, lịch sử hội thoại và câu hỏi) và số token đầu ra mà model sinh mới. Thông thường, đơn giá của token đầu ra đắt hơn đáng kể so với token đầu vào, nên câu trả lời dài làm chi phí tăng nhanh.

## D01-V01-06 | Chọn hạng model theo độ khó công việc thay vì luôn dùng model lớn
Model lớn mạnh về suy luận phức tạp nhưng chạy chậm và đắt; model nhỏ rẻ hơn và phản hồi nhanh hơn nhiều. Với các tác vụ đơn giản, lặp lại hoặc đã có khuôn mẫu rõ (phân loại ý định, trích xuất từ khoá, tóm tắt ngắn), nên chọn model nhỏ để tối ưu chi phí và độ trễ; chỉ dùng model lớn khi bài toán đòi hỏi suy luận nhiều bước hoặc ràng buộc tinh vi.

## D01-V01-07 | Mốc kiến thức (cutoff) và hiện tượng model bịa thông tin (hallucination)
Model chỉ học từ dữ liệu tới một mốc thời gian huấn luyện nhất định (knowledge cutoff), nên không tự biết các sự kiện mới xảy ra sau mốc đó (như chuyện tuần trước) nếu không có công cụ tra cứu ngoài. Khi thiếu dữ liệu, model vẫn có thể ghép chữ theo xác suất để tạo ra câu trả lời nghe rất tự tin nhưng sai sự thật — hiện tượng này gọi là bịa thông tin (hallucination), luôn cần kiểm chứng lại nguồn.

## D01-V01-08 | Cơ chế attention giúp model liên kết các phần trong ngữ cảnh
Cơ chế tự chú ý (attention) cho phép mô hình cân nhắc mức độ liên quan giữa từng token với các token khác trong cùng đoạn văn bản đầu vào, thay vì chỉ nhìn từng từ đứng sát nhau. Nhờ attention, model hiểu được đại từ thay thế cho danh từ nào ở đầu câu và nắm được mạch ý chính trên cả đoạn dài.

## D01-V02-01 | Mỗi vòng sinh tạo ra một token tiếp theo (generation loop)
Model không viết ra cả đoạn văn trong một bước duy nhất mà chạy vòng lặp sinh tự hồi quy: mỗi vòng nhận chuỗi ngữ cảnh hiện tại và dự đoán đúng một token tiếp theo, rồi nối token đó vào cuối để chạy vòng kế tiếp. Vì mỗi vòng sinh một token, một câu trả lời dài 50 token sẽ cần khoảng 50 vòng sinh liên tiếp.

## D01-V02-02 | Model dự đoán phân phối xác suất rồi mới chọn token kế tiếp
Tại mỗi vòng sinh, mạng nơ-ron tính điểm số thô (logits) cho toàn bộ từ điển rồi quy đổi qua hàm softmax thành phân phối xác suất cho từng token ứng viên. Nhờ xác suất này, nhiều phương án hợp lý đều có trọng số khác nhau trước khi hệ thống quyết định bốc token nào.

## D01-V02-03 | Temperature chỉnh độ ổn định và độ ngẫu nhiên khi chọn token
Tham số `temperature` điều chỉnh độ tập trung của phân phối xác suất trước khi bốc token tiếp theo. Khi `temperature` thấp (gần 0), model ưu tiên lặp lại phương án có xác suất cao nhất nên kết quả rất ổn định qua các lần chạy; khi `temperature` cao hơn, các token ít phổ biến hơn có cơ hội được chọn, tạo ra câu trả lời đa dạng hơn nhưng dễ lệch ý hơn.

## D01-V02-04 | Temperature = 0 chỉ tăng độ ổn định, không bảo đảm câu trả lời đúng
Đặt `temperature = 0` giúp model ít dao động và cho kết quả nhất quán giữa các lần hỏi giống nhau, nhưng không biến câu trả lời thành sự thật. Nếu câu hỏi vượt quá mốc kiến thức hoặc tài liệu đầu vào sai/thiếu, model để `temperature = 0` vẫn trả lời sai một cách rất ổn định; độ đúng phải dựa vào căn cứ dữ liệu.

## D01-V02-05 | Điều kiện dừng vòng lặp sinh và giới hạn max_tokens
Vòng lặp sinh token chỉ dừng khi gặp ký hiệu kết thúc câu (`EOS`), chạm chuỗi dừng (`stop sequence`) hoặc chạm trần `max_tokens`. Nếu câu trả lời vượt quá `max_tokens`, vòng lặp bị ngắt ngang và chữ đầu ra bị cụt giữa chừng; nên xem `max_tokens` là trần bảo vệ chi phí, không phải cách chỉnh độ dài đẹp.

## D01-V03-01 | Context window là tổng sức chứa token trong một lượt gọi
Context window (cửa sổ ngữ cảnh) là giới hạn tổng số token tối đa mà model có thể đọc và xử lý trong một lượt gọi, bao gồm cả phần đầu vào (system prompt, lịch sử hội thoại, tài liệu tra cứu, câu hỏi) lẫn phần đầu ra sắp sinh. Phần vượt quá giới hạn này sẽ bị cắt bỏ hoặc báo lỗi tuỳ ứng dụng.

## D01-V03-02 | Context window to hơn không tự làm model thông minh hơn
Một hiểu nhầm hay gặp là model có context window lớn sẽ tự động trả lời thông minh và chính xác hơn. Thực tế, nhồi quá nhiều chữ không liên quan vào ngữ cảnh dễ làm loãng sự chú ý (attention) của model, tăng thời gian chờ và đội chi phí mỗi lượt gọi; hiệu quả nằm ở việc chọn lọc đúng đoạn liên quan và giữ ngữ cảnh gọn gàng.

## D01-V03-03 | Phân bổ ngân sách ngữ cảnh và giữ "bàn làm việc" sạch
Ứng dụng AI tốt luôn chủ động chia ngân sách token trong context window cho từng phần: hướng dẫn cốt lõi, vài đoạn tài liệu thật sự khớp câu hỏi, và phần lịch sử hội thoại gần nhất. Thay vì nhét cả tài liệu dài vào prompt, cần tóm tắt hoặc chỉ nạp các đoạn vừa đủ để "bàn làm việc" của model gọn và ít nhiễu.

## D01-V03-04 | Agent kết hợp vòng lặp suy luận với công cụ ngoài
Khác với một lượt hỏi-đáp đơn lẻ, agent là ứng dụng cho phép model gọi các công cụ bên ngoài (như tra cứu đoạn bài, đọc dữ liệu) trong một vòng lặp có kiểm soát trước khi chốt câu trả lời cuối. Tuy nhiên, nếu bài toán chỉ cần tra tài liệu rồi trả lời theo khuôn mẫu cố định, workflow cố định thường rẻ hơn và dễ kiểm soát hơn nhiều so với agent tự do.

## D01-V03-05 | Chặn rủi ro bằng căn cứ mã đoạn và biết nói "không có trong bài"
Để tránh model tự suy diễn khi hỗ trợ học tập, hệ thống phải tra cứu các đoạn bài phù hợp trước, yêu cầu model chỉ dựa vào đó và gắn rõ mã đoạn nguồn cạnh giải thích. Khi câu hỏi nằm ngoài tài liệu đã có hoặc thiếu chi tiết cụ thể, câu trả lời đúng là nói rõ bài không có thông tin thay vì tự đoán con số hay chi tiết.
