n = 8
a = 1
b = 2

import math

def solution(n,a,b):
    answer = 0
    x = min(a, b)
    y = max(a, b)

    m = int(math.log2(n))
    c = 1
    mid = 2**(m-c)
    while 1:
        if x <= mid and y > mid:
            answer = m-c+1
            break
        else:
            c += 1
            if x <= mid and y <= mid:
                mid -= (2**(m-c))
            else:
                mid += (2**(m-c))

    print(answer)
    return answer

print(solution(n, a, b))