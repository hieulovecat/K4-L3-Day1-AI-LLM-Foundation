# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> khi giá trị càng tiến về 0, câu trả lời càng cứng nhắc, rập khuôn và mang tính thực tế. Khi temperature tăng dần lên 1.0, câu trả lời đa dạng và sáng tạo hơn. Ở mức quá cao như 1.5, phản hồi có xu hướng lan man, dùng từ ngữ kỳ lạ và độ chính xác giảm. TUy nhiên nếu hỏi những câu mà fact nó phổ biến, rộng rãi ở nhiều tài liệu trên thế giới thì giá trị temperature không khác nhau lắm

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
>  Em sẽ đặt temperature ở mức thấp (khoảng 0.0 đến 0.3). Vì chatbot hỗ trợ khách hàng cần sự chính xác, nhất quán và tuân thủ đúng chính sách của công ty thay vì sự bay bổng, bốc phét linh tinh. Việc giữ temperature thấp giúp giảm tối đa rủi ro chatbot bịa đặt thông tin sai lệch cho khách hàng.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> - GPT-4o đắt hơn GPT-4o-mini khoảng 16.7 lần (giá output $0.010 so với $0.0006 trên 1K token).
> - **Trường hợp GPT-4o xứng đáng:** Các tác vụ yêu cầu tư duy logic phức tạp, lập trình, giải quyết vấn đề khó, dịch thuật chuyên sâu hoặc khi cần chất lượng phản hồi hoàn hảo nhất.
> - **Trường hợp nên dùng mini:** Các tác vụ đơn giản, lặp đi lặp lại như phân loại văn bản (classification), trích xuất thông tin, tóm tắt đoạn văn hoặc khi cần xử lý một lượng lớn dữ liệu với chi phí tối ưu.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> - Khi đóng vai giáo viên tiểu học, model dùng từ vựng rất đơn giản, câu văn ngắn gọn và dùng các ví dụ trực quan để hình dung ra, dễ hiểu như cuốn sổ cái, viên bi. Tuy nhiên tôi đọc thì vẫn thấy khó hiểu đối với trẻ 8 tuổi :D
> - Khi đóng vai chuyên gia, model dùng rất nhiều thuật ngữ chuyên ngành (Decentralization, node, hash,...), câu văn dài và phân tích rất chuyên sâu.
> - Điều này cho thấy System Prompt có quyền lực rất lớn, giúp định hình toàn bộ phong cách trả lời, vốn từ vựng, mức độ chi tiết và đối tượng mà AI đang giao tiếp.


### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> - Em đã test với đoạn văn 106 từ, số token ước lượng là 141 nhưng đếm bằng tiktoken (chuẩn GPT-4o) thì chỉ có 133 token (chênh lệch khoảng 6%).
> - Về lý thuyết, tiếng Việt thường tốn nhiều token hơn tiếng Anh vì các bộ tokenizer cũ chủ yếu huấn luyện trên tiếng Anh. Các từ có dấu tiếng Việt thường bị băm nhỏ thành 2-3 token. Tuy nhiên, kết quả thực tế trên cho thấy bộ mã hóa mới của GPT-4o (o200k_base) đã tối ưu hóa cho tiếng Việt rất xuất sắc, khiến chi phí token được giảm xuống đáng kể và vô cùng sát với ước lượng.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> - **Streaming phù hợp** khi xây dựng các ứng dụng tương tác trực tiếp với người dùng cuối (như Chatbot, AI Assistant). Vì model mất khá nhiều thời gian để sinh ra toàn bộ văn bản, streaming giúp người dùng đọc được ngay những từ đầu tiên (giảm cảm giác chờ đợi, tăng trải nghiệm UX rất nhiều). Cảm giác nó như đang nói chuyện trực tiếp với user :PP
> - **Non-streaming phù hợp** trong các quy trình chạy ngầm (background jobs) hoặc các luồng xử lý tự động (như tóm tắt văn bản hàng loạt, AI phân tích dữ liệu, chấm điểm tự động). Ở những trường hợp này, hệ thống không có người dùng ngồi chờ đọc từng chữ mà chỉ cần lấy kết quả cuối cùng ở định dạng chuẩn (ví dụ xuất file JSON). Kiểu người ta cho AI làm việc xong người ta làm việc khác, chờ 1 lúc quay lại xem kết quả chứ đâu rảnh xem quá trình nó làm như nào :PP

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Thay vì liên tục "nã đạn" vào một server đang bị quá tải, việc tăng dần thời gian chờ sau mỗi lần thất bại (0.1s, 0.2s, 0.4s...) giúp giãn cách các request ra, cho server có thời gian "thở" để phục hồi hệ thống. Nếu dùng delay cố định, hàng nghìn client cùng bị văng ra và cùng thử lại đúng 1 giây sau đó, chúng sẽ tạo ra một hiện tượng gọi là "Thundering Herd" (Bầy đàn xô đẩy). Một lượng khổng lồ request đổ ập vào server cùng một lúc sẽ làm server sập hẳn luôn thay vì phục hồi. Giải pháp tốt nhất là nâng cấp server :PP

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> "Bạn là trợ giảng lập trình thân thiện. Hãy trả lời cực kỳ ngắn gọn, đi thẳng vào trọng tâm và luôn dùng tiếng Việt, trừ khi người dùng hỏi về code." Cụm từ "cực kỳ ngắn gọn, đi thẳng vào trọng tâm" giúp ép model không viết lan man dài dòng, từ đó tiết kiệm lượng token đầu ra (giảm chi phí API). Cụm "luôn dùng tiếng Việt" giúp ngăn tình trạng model tự ý chuyển sang tiếng Anh khi gặp các từ khóa kỹ thuật.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> - **Hạn chế:** Trợ lý bị giới hạn bộ nhớ (chỉ nhớ 3 lượt gần nhất), nên nếu hỏi lại một chi tiết từ đầu buổi chat, nó sẽ quên sạch. Hơn nữa, nó thiếu khả năng lưu trữ thông tin vĩnh viễn (nếu tắt terminal là mất trắng).
> - **Cách cải thiện:** Xây dựng tính năng "Bộ nhớ dài hạn" (Long-term Memory). Cách triển khai là tạo một file `.json` hoặc database nhỏ (như SQLite). Thay vì vứt bỏ các tin nhắn cũ, ta có thể dùng một model nhỏ tóm tắt lại toàn bộ lịch sử trò chuyện rồi nhét phần tóm tắt đó vào System Prompt. Bằng cách này, bot vừa nhớ được ý chính của cả phiên làm việc, vừa không làm phình to số token ở mỗi lượt gọi API.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
