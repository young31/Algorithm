# input
## 1
# n, m = 4, 5
# tl = [
#     [0, 0, 1, 1, 0],
#     [0, 0, 0, 1, 1],
#     [1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0]
# ]
# answer: 3

## 2
n, m = 15, 14
tl = [
    [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
    [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
]
# answer: 8

# algo
from copy import deepcopy
from collections import deque

visited = deepcopy(tl)
available_move = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def is_feasible(cur, move):
    i, j = cur
    di, dj = move
    if 0 <= i + di < n and 0 <= j + dj < m and visited[i+di][j+dj]==0:
        return True
    return False

def visit(cur):
    global visited
    i, j = cur
    visited[i][j] = 1
    for di, dj in available_move:
        if is_feasible(cur, (di, dj)):
            visit((i+di, j+dj))

def main():
    ans = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                visit((i, j))
                ans += 1
        
    print(ans)

main()
