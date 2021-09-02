from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    while que:
        d_cur, cur = heapq.heappop(que)
        if dist[cur] < d_cur:
            continue

        for j, d_nxt in graph[cur].items():
            d_new = d_cur + d_nxt
            if d_new < dist[j]:
                dist[j] = d_new
                heapq.heappush(que, (d_new, j))
                history[j] = [j] + history[cur]
    return dist

n = int(input())
m = int(input())

def inf(): return float('inf')
graph = {i: defaultdict(inf) for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

START, END = map(int, input().split())

history = {i: [i] for i in range(1, n+1)}

dist = dijkstra(START)
print(dist[END])
print(len(history[END]))
print(*history[END][::-1])