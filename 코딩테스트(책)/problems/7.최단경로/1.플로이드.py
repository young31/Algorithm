# input
n = 5; m = 14
graph = [
    [1, 2, 2],
    [1, 3, 3],
    [1, 4, 1],
    [1, 5, 10],
    [2, 4, 2],
    [3, 4, 1],
    [3, 5, 1],
    [4, 5, 3],
    [3, 5, 10],
    [3, 1, 8],
    [1, 4, 2],
    [5, 1, 7],
    [3, 4, 2],
    [5, 2, 4]
]
# answer: 
# 0 2 3 1 4
# 12 0 15 2 5
# 8 5 0 1 1
# 10 7 13 0 3
# 7 4 10 6 0

# algo
def solution(n, m, graph):
    inf = int(1e10)
    mat = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mat[i][i] = 0

    for a, b, c in graph:
        mat[a-1][b-1] = min(c, mat[a-1][b-1])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])

    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=' ')
        print()

solution(n, m, graph)
