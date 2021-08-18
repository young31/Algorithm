from collections import deque, defaultdict
from copy import deepcopy
import sys
input = sys.stdin.readline

moves = [
    (1, 0), (-1, 0), (0, 1), (0, -1)
]

n, m = map(int, input().split())
arr = [
    list(map(int, list(input().strip()))) for _ in range(n)
]

answer = deepcopy(arr)

groups = [
    [-1 for _ in range(m)] for _ in range(n)
]

group_value = defaultdict(int)
gn = -1
visited = [
    [False for _ in range(m)] for _ in range(n)
]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            gn += 1
            que = deque([(i, j)])
            cnt = 1
            visited[i][j] = True
            groups[i][j] = gn
            while que:
                i, j = que.popleft()
                for di, dj in moves:
                    ni = i+di
                    nj = j+dj
                    if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and not visited[ni][nj]:
                        que.append((ni, nj))
                        cnt += 1
                        visited[ni][nj] = True
                        groups[ni][nj] = gn
            group_value[gn] += cnt
            
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            used = set()
            for di, dj in moves:
                ni = i+di
                nj = j+dj
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and groups[ni][nj] not in used:
                    answer[i][j] += group_value[groups[ni][nj]]
                    used.add(groups[ni][nj])

for a in answer:
    b = list(map(lambda x: x%10, a))
    print(''.join(map(str, b)))
