def solution(a, b):
    a, b = min(a, b), max(a, b)
    answer = sum(range(a, b+1))
    return answer