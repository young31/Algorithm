import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

ans = defaultdict(int)

moves = [
    (1, 0), (-1, 0), (0, 1), (0, -1)
]
c = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y] and arr[x][y] > 0:
            c += 1
            que = deque([(x, y)])
            visited[x][y] = True
            while que:
                i, j = que.pop()
                ans[c] += 1
                for di, dj in moves:
                    ni = i+di
                    nj = j+dj
                    if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and arr[ni][nj] > 0:
                        que.append((ni, nj))
                        visited[ni][nj] = True

print(len(ans))
vs = sorted(ans.values())
for v in vs: print(v)