from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def inf(): return float('inf')

graph = {i: defaultdict(inf) for i in range(n+1)}
for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

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

s1 = 1
s2, s3 = map(int, input().split())

d1 = dijkstra(s1)
d2 = dijkstra(s2)
d3 = dijkstra(s3)

cand1 = d1[s2] + d2[s3] + d3[n]
cand2 = d1[s3] + d3[s2] + d2[n]

ans = min(cand1, cand2)
if ans == float('inf'):
    print(-1)
else:
    print(ans)