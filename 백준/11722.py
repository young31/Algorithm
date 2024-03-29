n = int(input())

nums = list(map(int, input().split()))
nums.reverse()

lens = [0 for _ in range(n)]
memo = {}

for i in range(n):
    if i == 0:
        lens[0] = 1
        memo[nums[i]] = 1
    else:
        m = nums[i]
        # 각 숫자마다 가장 최근이 어디인지 저장
        k = sorted(filter(lambda x: x < m, memo.keys()), key=memo.get)
        if k:
            lens[i] = memo[k[-1]]+1
            memo[m] = lens[i]
        else:
            lens[i] = 1
            memo[m] = 1
print(max(lens))