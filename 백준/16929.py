import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [
    list(input()) for _ in range(n)
]

visited = [[False for _ in range(m)] for _ in range(n)]

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

ans = False

def search(arr, cur, c, s):
    global ans
    if not ans:
        i, j = cur
        si, sj = s
        for di, dj in moves:
            ni = i+di
            nj = j+dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == arr[si][sj]:
                if ni == si and nj == sj and c >= 4:
                    ans = True
                    return
                elif not visited[ni][nj]:
                    visited[ni][nj] = True
                    search(arr, (ni, nj), c+1, s)
                    visited[ni][nj] = False

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            s = arr[i][j]
            search(arr, (i, j), 1, (i, j))
            if ans:
                print('Yes')
                exit()

if not ans:
    print('No')

                        
