n = int(input())
nums = list(map(int, input().split( )))

ans = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        ans[i] = nums[i]
    else:
        ans[i] = max(nums[i]+ans[i-1], nums[i])

print(max(ans))