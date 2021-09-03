from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def prim(start=1):
    visited = [False for _ in range(n+1)]
    dist = []
    heapq.heappush(dist, (0, start, start))
    total_weights = 0

    while dist:
        c, past, cur = heapq.heappop(dist)

        if not visited[cur]:
            visited[cur] = True
            total_weights += c

            for nxt, cost in graph[cur].items():
                print(cur, cost, nxt)
                if not visited[nxt]:
                    heapq.heappush(dist, (cost, cur, nxt))
    
    print(total_weights)

n = int(input())
m = int(input())

def inf(): return float('inf')
graph = {i: defaultdict(inf) for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

prim()