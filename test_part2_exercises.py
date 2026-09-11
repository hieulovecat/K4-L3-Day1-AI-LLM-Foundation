import os
from template import chat_with_system_prompt, count_tokens

print("="*50)
print("TEST CÂU 2.1: SỨC MẠNH CỦA PERSONA")
print("="*50)

question = "Giải thích blockchain là gì?"
prompt_1 = "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
prompt_2 = "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

print(f"\n[Giáo viên tiểu học] - System Prompt: '{prompt_1}'")
text_1, _ = chat_with_system_prompt(prompt_1, question)
print(f"Câu trả lời:\n{text_1}\n")

print(f"\n[Chuyên gia tài chính] - System Prompt: '{prompt_2}'")
text_2, _ = chat_with_system_prompt(prompt_2, question)
print(f"Câu trả lời:\n{text_2}\n")


print("="*50)
print("TEST CÂU 2.2: TIKTOKEN VS ĐẾM TỪ")
print("="*50)

doan_van_vn = (
    "Trí tuệ nhân tạo (AI) đang thay đổi cách chúng ta làm việc và sinh hoạt mỗi ngày. "
    "Từ việc gợi ý bài hát yêu thích, dịch thuật ngôn ngữ, đến việc hỗ trợ y bác sĩ chẩn đoán bệnh tật, "
    "AI mang lại nhiều lợi ích to lớn. Tuy nhiên, sự phát triển nhanh chóng của công nghệ này cũng đặt ra "
    "nhiều thách thức về bảo mật, đạo đức và việc làm. Chúng ta cần học cách làm chủ công nghệ thay vì để nó "
    "kiểm soát, nhằm tạo ra một tương lai bền vững và tốt đẹp hơn cho thế hệ mai sau."
)

word_count = len(doan_van_vn.split())
estimated_tokens = int(word_count / 0.75)
tiktoken_count = count_tokens(doan_van_vn)

print(f"Đoạn văn có {word_count} từ.")
print(f"1. Số token tính theo công thức ước lượng (số từ / 0.75): {estimated_tokens} tokens")
print(f"2. Số token đếm bằng thư viện tiktoken: {tiktoken_count} tokens")

if tiktoken_count > 0:
    diff_percent = abs(tiktoken_count - estimated_tokens) / tiktoken_count * 100
    print(f"-> Chênh lệch: {diff_percent:.2f}%\n")
