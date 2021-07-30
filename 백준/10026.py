from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [
    list(input()) for _ in range(n)
]

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

ans = []

def search(mode):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                cnt += 1
                que = deque()
                que.append((x, y))
                color = arr[x][y]
                if mode == 1:
                    if color in ['R', 'G']:
                        color = 'RG'
                while que:
                    i, j = que.popleft()
                    for di, dj in moves:
                        ni = i+di
                        nj = j+dj
                        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and arr[ni][nj] in color:
                            que.append((ni, nj))
                            visited[ni][nj] = True
    return cnt

print(search(0), search(1))