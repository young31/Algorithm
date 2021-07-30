from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

que = deque()
que.append((0, 0, 0))
visited[0][0] = True


while que:
    i, j, c = que.popleft()
    if i == n-1 and j == m-1:
        print(c+1)
        break
    for di, dj in moves:
        ni = i+di
        nj = j+dj
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj]==1 and not visited[ni][nj]:
            que.append((ni, nj, c+1))
            visited[ni][nj] = True
