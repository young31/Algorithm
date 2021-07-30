N = int(input())

dp = [1, 1, 1]
for _ in range(N):
    n = int(input())
    for i in range(n-len(dp)):
        dp.append(dp[-2]+dp[-3])
    print(dp[n-1])
