maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

from pprint import pprint

from collections import deque

move = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    pprint(maps)

    visited = [[False]*m for _ in range(n)]
    que = deque([(0, 0, 1)])
    visited[0][0] = True

    while que:
        i, j, c = que.popleft()
        
        for di, dj in move:
            ni = i+di
            nj = j+dj

            if ni == n-1 and nj == m-1:
                return c+1

            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and maps[ni][nj] == 1:
                que.append((ni, nj, c+1))
                visited[ni][nj] = True

    return -1


print(solution(maps))