n = 5
money = [1,2,5]


def solution(n, money):
    answer = 0
    dp = [0]*(n+1)
    for m in money:
        dp[m] = 1

    for i in range(n+1):
        for m in money:
            if 0 < i-m:
                dp[i] = max(dp[i], dp[i-m]+1)
    print(dp)
    return answer

solution(n, money)