from collections import deque

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    dp = deque([1, 1], maxlen=2)
    k = 2
    while k != n:
        dp.append(dp[0]*2 + dp[1]-dp[0])
        k += 1
    print(dp[-1])