# 전화번호 목록 Level 2

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for pb1, pb2 in zip(phone_book, phone_book[1:]):
        if pb2.startswith(pb1):
            answer = False
            break
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))