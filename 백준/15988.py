from collections import deque
import sys

def solution(x):
    global memo
    if x < 4:
        return memo[x-1]
    else:
        for k in range(4, x+1):
            if k not in memo.keys():
                s = memo[k-1] + memo[k-2] + memo[k-3]
                memo[k] = s % 1000000009
        return memo[x]

n = int(input())
memo = {1: 1, 2: 2, 3: 4}
for _ in range(n):
    q = int(sys.stdin.readline().strip())
    if q in memo.keys():
        ans = memo[q]
    else:
        ans = solution(q)
    print(ans % 1000000009)