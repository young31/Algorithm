from collections import deque
import sys
input = sys.stdin.readline

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

n, m = map(int, input().split())
board = [
    list(input().strip()) for _ in range(n)
]

visited = [[False for _ in range(m)] for _ in range(n)]

# 시간 마다 물이 차는 곳을 먼저 기록
que = deque([])
for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            que.append((i, j, 0))
            visited[i][j] = True
        if board[i][j] == 'S':
            s = (i, j)
        elif board[i][j] == 'D':
            d = (i, j)

while que:
    i, j, c = que.popleft()
    for di, dj in moves:
        ni = i+di
        nj = j+dj
        if 0 <= ni < n and 0 <= nj < m  and not visited[ni][nj] and board[ni][nj] not in ['D', 'S', 'X']:
            que.append((ni, nj, c+1))
            board[ni][nj] = c+1
            visited[ni][nj] = True

# 물 차는 기록을 알고 있으니까 물 차기 전에만 들어갈 수 있도록 탐색
visited = [[False for _ in range(m)] for _ in range(n)]
que = deque()
que.append(s+(0, ))
visited[s[0]][s[1]] = True

while que:
    i, j, c = que.popleft()
    for di, dj in moves:
        ni = i+di
        nj = j+dj
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and board[ni][nj] not in ['*', 'X']:
            if board[ni][nj] == 'D':
                print(c+1)
                exit()
            elif board[ni][nj] == '.' or board[ni][nj] > c+1:
                que.append((ni, nj, c+1))
                visited[ni][nj] = True

print('KAKTUS')
