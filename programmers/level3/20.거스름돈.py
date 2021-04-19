from pprint import pprint

n = 5
money = [1,2,5]


def solution(n, money):
    answer = 0
    money.sort()
    dp = [[0]*(n+1) for _ in range(len(money))]

    for i, c in enumerate(money):
        if c > n:
            break
        if i == 0:
            for j in range(1, n+1):
                if j % c == 0:
                    dp[i][j] = 1

        else:
            for j in range(1, n+1):
                if j < c:
                    dp[i][j] = dp[i-1][j]
                elif j == c:
                    dp[i][j] = dp[i-1][j]+1
                else:
                    dp[i][j] = dp[i-1][j] + max(dp[i-1][j-c], dp[i][j-c])
        pprint(dp)
        print()

    for i in range(len(money)):
        if dp[i][-1] > answer:
            answer = dp[i][-1]
    print(answer)
    return answer

solution(n, money)