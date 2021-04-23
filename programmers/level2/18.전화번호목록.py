phone_book = ["119", "97674223", "1195524421"]

def check(a, b):
    n = len(a)
    if len(b) < n:
        return False
    else:
        return True if a == b[:n] else False

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i, p in enumerate(phone_book[:-1]):
        reg = f'^{p}'
        if check(p, phone_book[i+1]):
            return False
    return answer

print(solution(phone_book))
