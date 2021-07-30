from collections import defaultdict, deque
from itertools import combinations, product
from pprint import pprint
import sys
input = sys.stdin.readline

n = int(input())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

visited = [[False for _ in range(n)] for _ in range(n)]

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

ter = defaultdict(list)
ter_n = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and not visited[i][j]:
            que = deque([(i, j)])
            ter[ter_n].append((i, j))
            while que:
                x, y = que.popleft()
                for di, dj in moves:
                    ni = x+di
                    nj = y+dj
                    if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and arr[ni][nj] != 0:
                        que.append((ni, nj))
                        visited[ni][nj] = True
                        ter[ter_n].append((ni, nj))
                        arr[ni][nj] = ter_n
            ter_n += 1

ans = float('inf')

# for k in ter.keys():
#     for i, j in ter[k]:
#         visited = [[False for _ in range(n)] for _ in range(n)]
#         que = deque([(i, j, 0)])
#         visited[i][j] = True
#         while que:
#             x, y, c = que.popleft()
#             if c >= ans:
#                 break
#             for di, dj in moves:
#                 ni = x+di
#                 nj = y+dj
#                 if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
#                     if arr[ni][nj] not in [0, k]:
#                         ans = min(ans, c)

#                     elif arr[ni][nj] == 0 and c+1 < ans:
#                         que.append((ni, nj, c+1))


for a, b in combinations(ter.keys(), 2):
    for a_, b_ in product(ter[a], ter[b]):
        ans = min(abs(a_[0]-b_[0])+abs(a_[1]-b_[1])-1, ans)

print(ans)