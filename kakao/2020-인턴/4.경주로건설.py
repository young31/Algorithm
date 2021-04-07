# 미해결

# input
board = [[0,0,0],[0,0,0],[0,0,0]]

# answer: 3800

# algo
from collections import deque
from pprint import pprint

moves_h = [
    (0, 1, 'p'), (0, -1, 'p')
]

moves_v = [
    (1, 0, 'v'), (-1, 0, 'v')
]

def is_feasible(board, a):
    n = len(board)
    x, y = a
    if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
        return True
    return False

def solution(board):
    answer = 0
    n = len(board)
    inf = int(1e9)
    scores = [[inf]*n for _ in range(n)]
    scores[0][0] = 0
    scores[1][0] = 100
    scores[0][1] = 100

    visited = [[False]*n for _ in range(n)]

    que = deque([(0, 0, 0, 'h'), (0, 0, 0, 'v')])
    while que:
        a = que.popleft()
        x, y, s, head = a
        visited[x][y] = True

        for dx, dy, h in moves_h:
            nx, ny = x+dx, y+dy
            if is_feasible(board, (nx, ny)) and (scores[nx][ny] >= scores[x][y]+100 or not visited[nx][ny]):
                if h == head:
                    score = min(scores[nx][ny], scores[x][y]+100)
                else:
                    score = min(scores[nx][ny], scores[x][y]+600)

                scores[nx][ny] = score
                que.append((nx, ny, score, h))

        for dx, dy, h in moves_v:
            nx, ny = x+dx, y+dy
            if is_feasible(board, (nx, ny)) and (scores[nx][ny] >= scores[x][y]+100 or not visited[nx][ny]):
                if h == head:
                    score = min(scores[nx][ny], scores[x][y]+100)
                else:
                    score = min(scores[nx][ny], scores[x][y]+600)

                scores[nx][ny] = score
                que.append((nx, ny, score, h))

    answer = scores[n-1][n-1]
    pprint(scores)
    return answer

solution(board)