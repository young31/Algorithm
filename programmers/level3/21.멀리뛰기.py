from functools import lru_cache
import sys

sys.setrecursionlimit(int(1e4))

@lru_cache()
def f(n):
    if n <= 2:
        return n
    return f(n-2) + f(n-1)
        
def solution(n):
    answer = f(n)
    return answer%1234567
print(solution(2000))