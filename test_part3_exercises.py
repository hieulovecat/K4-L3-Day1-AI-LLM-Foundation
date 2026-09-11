import os
from template import streaming_chatbot

print("="*50)
print("TEST CÂU 3.1: TRẢI NGHIỆM STREAMING")
print("="*50)
print("Hãy thử gõ vài câu hỏi (ví dụ: 'Xin chào', 'Kể một mẩu chuyện ngắn')")
print("để thấy model gõ từng chữ ra màn hình như thế nào nhé!")
print("Gõ 'quit' hoặc 'exit' để dừng.\n")

try:
    streaming_chatbot()
except Exception as e:
    print(f"\nLỗi: {e}")
    print("Vui lòng đảm bảo bạn đã cấu hình đúng file .env với API Key.")
