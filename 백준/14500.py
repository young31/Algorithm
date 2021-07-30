# 해결 안함

moves = [
    (1, 0), (-1, 0), (0, 1), (0, -1)
]
best = 0

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def find(i, j, k, c=0):
    global best, visited
    if c == 3 and k > best:
        best = k
        return
    
    for di, dj in moves:
        ni = i+di
        nj = j+dj
        if 0 <= ni < n and 0 <= nj < m and (ni, nj) and not visited[ni][nj]:
            visited[ni][nj] = True
            find(ni, nj, k+arr[ni][nj], c+1)
            visited[ni][nj] = False

for i in range(n):
    for j in range(m):
        find(i, j, arr[i][j])
print(best)
