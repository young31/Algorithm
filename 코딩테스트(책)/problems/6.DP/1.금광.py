# input
n1, m1 = 3, 4
mine1 = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]

n2, m2 = 4, 4
mine2 = [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]
# answer: 19, 16

# algo
from copy import deepcopy
from collections import deque

def deserialize(n, m, mine):
    res = []
    for i in range(0, n*m, m):
        res.append(mine[i:i+m])
    return res

def solution1(n, m, mine):
    # BFS
    mine = deserialize(n, m, mine)
    moves = [
        (-1, 1), (0, 1), (1, 1)
    ]
    cum = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        q = deque()
        j = 0
        cum[i][j] = mine[i][j]
        q.append((i, j))
        while len(q) > 0:
            i, j = q.popleft()
            for move in moves:
                ni = i+move[0]; nj = j+move[1]
                if 0 <= ni < n and 0 <= nj < m:
                    cum[ni][nj] = max(cum[i][j]+mine[ni][nj], cum[ni][nj])
                    q.append((ni, nj))

    max_ = 0
    for i in range(n):
        for j in range(m):
            if cum[i][j] > max_:
                max_ = cum[i][j]
    return max_

def solution2(n, m, mine):
    # DP
    def feasible_gold(i, j, mine):
        if 0 <= i < n and 0 <= j < m:
            return mine[i][j]
        else:
            return 0

    mine = deserialize(n, m, mine)
    cum = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        cum[i][0] = mine[i][0]
    
    for j in range(1, m):
        for i in range(n):
            cum[i][j] = max(
                feasible_gold(i-1, j-1, cum), feasible_gold(i, j-1, cum), feasible_gold(i+1, j-1, cum)
            ) + mine[i][j]

            # print(cum)

    max_ = 0
    for i in range(n):
        for j in range(m):
            if cum[i][j] > max_:
                max_ = cum[i][j]
    return max_


print('solution1')
print(solution1(n1, m1, mine1))
print(solution1(n2, m2, mine2))
print('solution2')
print(solution2(n1, m1, mine1))
print(solution2(n2, m2, mine2))




