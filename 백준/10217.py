# 어디가 틀렸지?
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, 0, start)) # time, cost, node
    dist = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
    dist[start][0] = 0
    while que:
        d_cur, t_cur, cur = heapq.heappop(que)
        if dist[cur][d_cur] < t_cur:
            continue

        for nxt, (t_nxt, d_nxt) in graph[cur].items():
            t_new = t_cur + t_nxt
            d_new = d_cur + d_nxt

            if d_new <= m:
                heapq.heappush(que, (d_new, t_new, nxt))
                if t_new < dist[nxt][d_new]:
                    dist[nxt][d_new] = t_new

                    for i in range(1, m+1):
                        dist[nxt][i] = t_new

    return dist

N = int(input())
for _ in range(N):
    n, m, k = map(int, input().split())

    graph = {i: {} for i in range(1, n+1)}

    for _ in range(k):
        a, b, c, t = map(int, input().split())
        graph[a][b] = (t, c)

    dist = dijkstra(1)
    ans = min(dist[n])
    if ans == float('inf'):
        print('Poor KCM')
    else:
        print(ans)