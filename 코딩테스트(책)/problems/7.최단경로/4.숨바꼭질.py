# input
n, m = 6, 7
edges = [
    (3, 6), (4, 3), (3, 2), (1, 3), (1, 2), (2, 4), (5, 2)
]

# answer: 4, 2, 3

# algo
def solution(n, edges):
    inf = int(1e9)
    dist_mat = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist_mat[i][i] = 0

    for i, j in edges:
        i -= 1
        j -= 1
        dist_mat[i][j] = 1
        dist_mat[j][i] = 1

    i = 0
    for k in range(n):
        for j in range(n):
            dist_mat[0][j] = min(dist_mat[i][j], dist_mat[i][k] + dist_mat[k][j])

    target_dist = [dist_mat[0][c] for c in range(n)]

    max_dis = max(target_dist)
    max_loc = target_dist.index(max_dis)+1
    count = target_dist.count(max_dis)

    print(max_loc, max_dis, count)

solution(n, edges)
