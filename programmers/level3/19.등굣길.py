m=4; n=3; puddles=[[2, 2]]

# bfs는 시간초과
from collections import deque

moves = [
    (1, 0), (0, 1)
]

def solution(m, n, puddles):
    answer = 0
    graph = [[0]*m for _ in range(n)]
    for a, b in puddles:
        graph[b-1][a-1] = 1
    
    if 1 in graph[0]:
        idx = graph[0].index(1)
        for i in range(idx, m):
            graph[0][i] = 1
    que = deque([])
    que.append((0, 0, 0))
    inf = int(1e9)
    dist = inf

    while que:
        i, j, c = que.popleft()
        for di, dj in moves:
            ni = i+di
            nj = j+dj
            if ni ==n-1 and nj==m-1:
                answer+=1
                break
            if 0 <= ni < n and 0 <= nj < m:
                if graph[ni][nj] != 1:
                    que.append((ni, nj, c+1))
    # print(answer)
    return answer%1000000007

solution(m, n, puddles)


def solution(m, n, puddles):
    answer = 0
    graph = [[0]*(m+1) for _ in range(n+1)]
    for a, b in puddles:
        graph[b][a] = -1
        
    graph[1][1] = 1

    for i in range(n+1):
        for j in range(m+1):

            if graph[i][j] != -1:
                ans = 0
                for di, dj in [(-1, 0), (0, -1)]:
                    ni = i+di
                    nj = j+dj
                    if graph[ni][nj] != -1:
                        ans += graph[ni][nj]

                graph[i][j] += ans%1000000007

    answer = graph[n][m]
    return answer%1000000007

solution(m, n, puddles)
