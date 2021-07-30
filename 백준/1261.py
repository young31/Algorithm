from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [
    list(map(int, list(input().strip()))) for _ in range(n)
]

visited = [[False for _ in range(m)] for _ in range(n)]
memo = [[float('inf') for _ in range(m)] for _ in range(n)]

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

que = deque()
que.append((0, 0, 0))
visited[0][0] = True
ans = float('inf')

if n == 1 and m == 1:
    print(0)
else:
    while que:
        i, j, c = que.popleft()

        for di, dj in moves:
            ni = i+di
            nj = j+dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 0:
                    if not visited[ni][nj] or memo[ni][nj] > c:
                        que.append((ni, nj, c))
                    memo[ni][nj] = min(memo[ni][nj], c)
                else:
                    if not visited[ni][nj] or memo[ni][nj] > c+1:
                        que.append((ni, nj, c+1))
                    memo[ni][nj] = min(memo[ni][nj], c+1)
                visited[ni][nj] = True

    print(memo[-1][-1])