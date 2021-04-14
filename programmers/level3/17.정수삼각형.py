triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0
    n = len(triangle)
    res = triangle.copy()
    for i in range(1, n):
        for j in range(i+1):
            l = max(j-1, 0)
            r = min(j, i-1)
            res[i][j] = max(res[i-1][l], res[i-1][r]) + res[i][j]
    answer = max(res[-1])
    print(res)
    return answer

solution(triangle)