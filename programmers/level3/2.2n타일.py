n = 4

import sys
sys.setrecursionlimit(int(1e6))
def solution(n):
    def recur(n):
        if n == 1:
            return 1
        elif n==2:
            return 2
        else:
            return solution(n-2) + solution(n-1)
    answer = recur(n)
    return answer%1000000007

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        n1 = 1
        n2 = 2
        for _ in range(n-2):
            n1, n2 = n2, n2+n1


    return n2%1000000007


print(solution(4))