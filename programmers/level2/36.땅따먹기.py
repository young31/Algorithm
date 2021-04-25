land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]


def solution(land):
    answer = 0
    indices = {i: [j for j in range(4) if i != j] for i in range(4)}
    print(indices)

    n = len(land)
    dp = [[0]*4 for _ in range(n)]
    dp[0] = land[0]

    for i in range(1, n):
        for j in range(4):
            i1, i2, i3 = indices[j]
            dp[i][j] = land[i][j] + max(dp[i-1][i1], dp[i-1][i2], dp[i-1][i3])
    
    answer = max(dp[-1])
    print(answer)
    return answer

solution(land)