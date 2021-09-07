# 아아디어 참고: 인접 좌표만 대상으로 해도 됨
## 시간 초과 pypy로 간신히 넘김
import heapq
from collections import defaultdict

def get_dist(x, y):
    x1, x2, x3 = x[:-1]
    y1, y2, y3 = y[:-1]
    res = min(abs(x1-y1), abs(x2-y2), abs(x3-y3))
    return res

def prim(start=0):
    visited = [False for _ in range(n)]
    dist = []
    heapq.heappush(dist, (0, start, start))
    total_weights = 0

    while dist:
        c, past, cur = heapq.heappop(dist)

        if not visited[cur]:
            visited[cur] = True
            total_weights += c

            for nxt in adj[cur]:
                if not visited[nxt]:
                    cost = get_dist(nodes[cur], nodes[nxt])
                    heapq.heappush(dist, (cost, cur, nxt))

    print(total_weights)

n = int(input())

nodes = [list(map(int, input().split())) + [i] for i in range(n)]

adj = defaultdict(set)

for l in range(3):
    nodes_x = sorted(nodes, key=lambda x: x[l])
    for i in range(1, n):
        adj[nodes_x[i][-1]].add(nodes_x[i-1][-1])
        adj[nodes_x[i-1][-1]].add(nodes_x[i][-1])

prim()