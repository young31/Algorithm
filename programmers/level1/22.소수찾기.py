def solution(n):
    def is_prime(x):
        if x == 1:
            return False
        m = int(x**0.5)+1
        for i in range(2, m):
            if x%i == 0:
                return False
        return True
    answer = 0
    for i in range(1, n+1):
        answer += is_prime(i)
    return answer