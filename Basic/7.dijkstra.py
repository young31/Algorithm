import heapq
from collections import defaultdict

# data init
n = 6
graph = [
    [0, 2, 5, 1, float('inf'), float('inf')],
    [2, 0, 3, 2, float('inf'), float('inf')],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, 5],
    [float('inf'), float('inf'), 1, 1, 0, 2],
    [float('inf'), float('inf'), 5, float('inf'), 2, 0]
]
graph_dct = defaultdict(dict)
for i in range(n):
    for j in range(n):
        if graph[i][j] != float('inf'):
            graph_dct[i][j] = graph[i][j]

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    while que:
        d_cur, nxt = heapq.heappop(que)
        if dist[nxt] < d_cur:
            continue

        for j, d_nxt in graph_dct[nxt].items():
            d_new = d_cur + d_nxt
            if d_new < dist[j]:
                dist[j] = d_new
                heapq.heappush(que, (d_new, j))
    print(dist)
    return dist

for i in range(n):
    dijkstra(i)