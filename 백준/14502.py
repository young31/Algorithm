from itertools import combinations
from copy import deepcopy
from collections import deque

moves = [
   (0, 1), (0, -1), (1, 0), (-1, 0) 
]

n, m = map(int, input().split())

arr = [
    list(map(int, input().split())) for _ in range(n)
]

zeros = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            zeros.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

def count(arr_, block):
    arr = deepcopy(arr_)
    for i, j in block:
        arr[i][j] = 1

    visited = [[False for _ in range(m)] for _ in range(n)]
    que = deque(virus)
    while que:
        i, j = que.popleft()
        visited[i][j] = True
        for di, dj in moves:
            ni = i+di; nj = j+dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and not visited[ni][nj]:
                arr[ni][nj] = 2
                visited[ni][nj] = True
                que.append((ni, nj))

    c = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                c += 1
    return c
    

answer = 0
for comb in combinations(zeros, 3):
    answer = max(answer, count(arr, comb))
print(answer)
