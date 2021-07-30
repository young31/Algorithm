import sys 
input = sys.stdin.readline
from collections import deque

moves = [
    (-1, -2), (-2, -1), (-2, 1), (-1, 2), 
    (1, -2), (2, -1), (2, 1), (1, 2)
]


N = int(input())
for _ in range(N):
    n = int(input())
    ai, aj = map(int, input().split())
    bi, bj = map(int, input().split())
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[ai][aj] = True
    que = deque([(ai, aj, 0)])
    while que:
        i, j, c = que.popleft()
        if i == bi and j == bj:
            print(c)
            break
        for di, dj in moves:
            ni = i+di
            nj = j+dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                que.append((ni, nj, c+1))
                visited[ni][nj] = True


