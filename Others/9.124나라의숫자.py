n = 4

def solution(n):
    import math

    table = {0: '1', 1: '2', 2: '4'}
    answer = ''
    i = 1
    m = 0
    while 1:
        m += 3**i
        if n <= m:
            m -= 3**i
            i -= 1
            break
        i = i + 1

    n_ = i
    for _ in range(n_+1):
        for j in range(2, -1, -1):
            if n > m+(3**i)*j:
                m = m+(3**i)*j
                answer += table[j]
                i -= 1
                break

    return answer

solution(n)