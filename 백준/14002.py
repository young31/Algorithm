n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]
memo = {}

for i in range(n):
    k = arr[i]
    tmp = sorted(filter(lambda x: x < k, memo.keys()), key=memo.get)
    if tmp:
        dp[i] = memo[tmp[-1]]+1
        memo[k] = dp[i]
    else:
        dp[i] = 1
        memo[k] = 1

max_ = max(dp)
print(max_)

for i, v in enumerate(arr):
    if memo[v] == max_:
        break

ans = []
for i in range(n-1, -1, -1):
    if dp[i] == max_:
        ans.append(arr[i])
        max_ -=1 

ans.reverse()
for a in ans: print(a, end=' ')