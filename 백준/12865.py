from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

items = [
    tuple(map(int, input().split())) for _ in range(n)
]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

idx = 1
for i, v in items:
    for j in range(k+1):
        if j-i >= 0:
            dp[idx][j] = max(dp[idx-1][j-i]+v, dp[idx-1][j])
        else:
            dp[idx][j] = dp[idx-1][j]
    idx += 1
print(dp)
print(dp[-1][-1])


