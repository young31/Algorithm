from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = int(input())

def inf(): return float('inf')

graph = {i: defaultdict(inf) for i in range(n+1)}
for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    while que:
        d_cur, nxt = heapq.heappop(que)
        if dist[nxt] < d_cur:
            continue

        for j, d_nxt in graph[nxt].items():
            d_new = d_cur + d_nxt
            if d_new < dist[j]:
                dist[j] = d_new
                heapq.heappush(que, (d_new, j))
    return dist

dist = dijkstra(t)

for c in dist[1:]:
    if c == float('inf'):
        print('INF')
    else:
        print(c)