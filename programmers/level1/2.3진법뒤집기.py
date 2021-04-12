n = 45

import math

def solution(n):
    n3 = []
    i = 0
    while n:
        a, b = n//3, n%3
        n3.append(b)
        n = a
        i += 1

    answer = 0
    i = len(n3)-1
    for j in n3:
        answer += j*(3**i)
        i -= 1
    print(answer)    
    return answer

solution(n)