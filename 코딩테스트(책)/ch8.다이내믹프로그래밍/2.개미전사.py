# input
n = 4
array = [1, 3, 1, 5]

# answer: 8

# algo
dp = [0 for _ in range(n)]

def cur_value(dp, idx):
    if idx <= 1:
        dp[idx] = array[idx]
    elif idx == 2:
        dp[idx] = array[0] + array[idx]
    else: # 순차적으로 채우기 // 완전탐색보다 현저히 빠름
        dp[idx] = max(array[idx-2], array[idx-3]) + array[idx]

    return dp

def main(dp):
    for i in range(n):
        dp = cur_value(dp, i)

    print(max(dp))

main(dp)