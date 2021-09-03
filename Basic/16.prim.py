# 무향 그래프에 사용
## edge가 많으면 kruskal 보다 유리함
import heapq

def prim(start=1):
    visited = [False for _ in range(n+1)]
    dist = []
    heapq.heappush(dist, (0, start, start))
    connected = []
    total_weights = 0

    while dist:
        c, past, cur = heapq.heappop(dist)

        if not visited[cur]:
            visited[cur] = True
            connected.append((past, cur))
            total_weights += c

            for cost, nxt in graph[cur]:
                if not visited[nxt]:
                    heapq.heappush(dist, (cost, cur, nxt))

    print(connected)
    print(total_weights)

n = 7
graph = {
    1: [(67, 2), (28, 4), (17, 5), (12, 7)],
    2: [(67, 1), (24, 4), (62, 5)],
    3: [(20, 5), (37, 6)],
    4: [(28, 1), (24, 2), (13, 7)],
    5: [(45, 6), (73, 7)],
    6: [],
    7: [],
}

for k, vs in graph.items():
    for c, v in vs:
        if (c, k) not in graph[v]:
            graph[v].append((c, k))

prim()