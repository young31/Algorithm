n = 4

def solution(n):
    if n%2 == 1:
        return 0
    div = 1000000007
    n2 = n//2
    dp = [3, 11, 41]
    if n2 <= 3:
        return dp[n2-1]
    for _ in range(n2-3):
        dp.append(dp[-1]*3 + dp[-2]*3 - dp[-3])
    answer = dp[-1]
    return answer%div

print(solution(10))