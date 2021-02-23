# https://programmers.co.kr/learn/courses/30/lessons/60063
# input
board = [
    [0, 0, 0, 1, 1], 
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

# answer: 7

# algo
## 몇 테케에서 시간초과가 난다.
## 코드는 크게 문제될게 없어보이는데 왜일지 모르겠다.
from collections import deque
visited = []

def feasible(x, board):
    n = len(board)
    if 0 <= x[0] < n and 0 <= x[1] < n and board[x[0]][x[1]] != 1:
        return True
    return False

def move(board, i, j):
    res = []
    available_move = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
    ]
    
    x1, y1 = i
    x2, y2 = j
    pos_type = 1 if x1==x2 else 2
    for c, (d1, d2) in enumerate(available_move):
        nx1, ny1 = x1+d1, y1+d2
        nx2, ny2 = x2+d1, y2+d2
        ni = (nx1, ny1); nj = (nx2, ny2)
        ni, nj = sorted([ni, nj])
        if feasible(ni, board) and feasible(nj, board) and ni+nj not in visited:
            yield ni, nj
            if pos_type == 1:
                if c == 0:
                    ni, nj = (x2, y2), (x1+1, y1+1)
                    if ni+nj not in visited:
                        yield ni, nj
                    ni, nj = (x1, y1), (x2+1, y2-1)
                    if ni+nj not in visited:
                        yield ni, nj
                elif c == 1:
                    ni, nj = (x1-1, y1+1), (x2, y2)
                    if ni+nj not in visited:
                        yield ni, nj
                    ni, nj = (x2-1, y2-1), (x1, y1)
                    if ni+nj not in visited:
                        yield ni, nj
            else:
                if c == 2:
                    ni, nj = (x2, y2), (x1+1, y1+1)
                    if ni+nj not in visited:
                        yield ni, nj
                    ni, nj = (x1, y1), (x2-1, y2+1)
                    if ni+nj not in visited:
                        yield ni, nj
                elif c == 3:
                    ni, nj = (x1+1, y1-1), (x2, y2)
                    if ni+nj not in visited:
                        yield ni, nj
                    ni, nj = (x1, y1), (x2-1, y2-1)
                    if ni+nj not in visited:
                        yield ni, nj

def solution(board):    
    memory = deque([(0, 0, 0, 1, 0)])
    n = len(board)
    while 1:
        ij = memory.popleft()
        i = ij[:2]
        j = ij[2:-1]
        i, j = sorted([i, j])
        cost = ij[-1]
        visited.append(i+j)

        for ni, nj in move(board, i, j):
            if (nj == (n-1, n-1)) or (ni == (n-1, n-1)):
                return cost+1

            memory.append(ni+nj+(cost+1, ))

print(solution(board))