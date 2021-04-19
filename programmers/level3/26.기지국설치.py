n = 16
stations = [9]
w = 2

import math

def solution(n, stations, w):
    answer = 0

    c = 2*w + 1
    l = 0
    for s in stations:
        a = max(s-w, 1)
        b = min(s+w, n)
        if a <= l+1:
            l = b
            continue

        answer += math.ceil((a-l-1)/c)
        l = b
        if l >= n:
            break

    if b <= n:
        answer += math.ceil((n-b)/c)

    return answer

solution(n, stations, w)