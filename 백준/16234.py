from collections import deque

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]


def find(arr, n, l, r):
    visited = [[False for _ in range(n)] for _ in range(n)]
    groups = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                x = i; y = j
                visited[i][j] = True
                que = deque([(i, j)])
                g = [(x, y)]
                while que:
                    print(que)
                    x, y = que.popleft()
                    for dx, dy in moves:
                        nx = x+dx; ny = y+dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                            que.append((nx, ny))
                            visited[nx][ny] = True
                            g.append((nx, ny))
                if len(g) > 1:
                    groups.append(g)
    return groups


n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
while 1:
    for a in arr: print(a)
    
    groups = find(arr, n, l, r)
    print(groups)
    print()
    if groups:
        cnt += 1
        for group in groups:
            total = 0
            c = 0
            for x, y in group:
                total += arr[x][y]
                c += 1
            new = total // c
            for x, y in group:
                arr[x][y] = new
    else:
        break
for a in arr: print(a)

print(cnt)