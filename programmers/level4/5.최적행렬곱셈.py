matrix_sizes = [[5,3],[3,10],[10,6]] # 270
matrix_sizes = [[10,6],[6,3],[3,2]] # 156
matrix_sizes = [[4,10],[10,2],[2,3],[3,4]] # 136

# keyword: matrix chain multiplication
def solution(matrix_sizes):
    answer = 0
    n = len(matrix_sizes)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    p = matrix_sizes[0].copy()
    for i in range(1, n):
        p.append(matrix_sizes[i][1])

    for l in range(1, n):
        for i in range(n-l):
            j = i+l
            dp[i][j] = min([dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1] for k in range(i, j)])

    answer = dp[0][-1]
    print(answer)
    return answer

solution(matrix_sizes)
