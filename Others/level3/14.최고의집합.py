n = 3
s = 11

def solution(n, s):
    if n > s:
        return [-1]

    k = s//n
    m = s - n*k
    answer = [k]*(n-m) + [k+1]*m
    print(k, m, answer)
    return answer

solution(n, s)