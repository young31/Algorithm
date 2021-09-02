n = int(input())

dp = [float('inf') for _ in range(n+1)]
hist = [[] for _ in range(n+1)]

dp[1] = 0
hist[1] = [1]

for i in range(2, n+1):
    d0 = dp[i]
    d1 = dp[i-1] + 1
    d2 = dp[i//2] + 1 if i%2 == 0 else float('inf')
    d3 = dp[i//3] + 1 if i%3 == 0 else float('inf')
    d = min(d0, d1, d2, d3)

    if d == d0:
        continue
    elif d == d1:
        hist[i] = hist[i-1]+[i]
    elif d == d2:
        hist[i] = hist[i//2]+[i]
    elif d == d3:
        hist[i] = hist[i//3]+[i]

    dp[i] = d

print(dp[n])
print(*hist[n][::-1])
# q = deque([1])
# dp = [float('inf') for _ in range(n+1)]
# hist = [[] for _ in range(n+1)]
# dp[1] = 0
# hist[1] = [1]

# while q:
#     cur = q.popleft()
#     if cur*3 <= n and dp[cur*3] > dp[cur]+1:
#         q.append(cur*3)
#         dp[cur*3] = dp[cur]+1
#         hist[cur*3] = hist[cur] + [cur*3]


#     if cur*2 <= n and dp[cur*2] > dp[cur]+1:
#         q.append(cur*2)
#         dp[cur*2] = dp[cur]+1
#         hist[cur*2] = hist[cur] + [cur*2]

#     if cur+1 <= n and dp[cur+1] > dp[cur]+1:
#         q.append(cur+1)
#         dp[cur+1] = dp[cur]+1
#         hist[cur+1] = hist[cur] + [cur+1]

# print(dp[n])
# print(*hist[n][::-1])