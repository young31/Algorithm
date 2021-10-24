from collections import deque
from itertools import combinations

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

viruses = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            viruses.append((i, j))

def is_done(visited):
    res = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                if not visited[i][j]:
                    return False
                else:
                    res = max(res, vv[i][j])
    return res

answer = float('inf')
for comb in combinations(viruses, m):
    visited = [[False for _ in range(n)] for _ in range(n)]
    vv = [[0 for _ in range(n)] for _ in range(n)]
    que = deque([])
    for c in comb: que.append((c[0], c[1], 0))

    while que:
        i, j, c = que.popleft()
        visited[i][j] = True
        for di, dj in moves:
            ni = i+di; nj = j+dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 1 and not visited[ni][nj]:
                que.append((ni, nj, c+1))
                visited[ni][nj] = True
                vv[ni][nj] = c+1

    res = is_done(visited)
    if res is not False:
        answer = min(answer, res)


if answer != float('inf'):
    print(answer)
else:
    print(-1)