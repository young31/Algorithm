import sys
input = sys.stdin.readline

n = int(input())
arr = [
    int(input()) for _ in range(n)
]

if n <= 2:
    print(sum(arr))
    exit()

dp = [
    [0 for _ in range(n)] for _ in range(3)
]

dp[0][0] = 0
dp[1][0] = arr[0]
dp[2][0] = arr[0]

for i in range(1, n):
    max_ = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
    dp[0][i] = max_
    dp[1][i] = dp[0][i-1]+arr[i]
    dp[2][i] = dp[1][i-1]+arr[i]

ans = max([dp[i][-1] for i in range(3)])
print(ans)