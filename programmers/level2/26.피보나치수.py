n = 10

from functools import lru_cache

@lru_cache()
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def solution(n):
    answer = fibo(n)
    return answer