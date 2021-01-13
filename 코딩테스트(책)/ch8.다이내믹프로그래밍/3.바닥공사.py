# input
n = 3
# answer: 5

# algo

dp = [0 for _ in range(n)]

def step(dp, i):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 3
    else:
        dp[i] = dp[i-2]*2 + dp[i-1]
    return dp

for i in range(n):
    dp = step(dp, i)

print(dp)