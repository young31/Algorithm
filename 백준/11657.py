from collections import defaultdict
import sys
input = sys.stdin.readline

def bellmanford(start):
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    # 최소거리 계산
    for rep in range(1, n+1): # n-1 번
        for node in graph.keys(): # 모든 노드에 대해서 
            for adj, d in graph[node].items():
                if dist[node] + d < dist[adj]:
                    dist[adj] = dist[node] + d
                    if rep == n:
                        return False

    return dist

def inf(): return float('inf')

n, m = map(int, input().split())

graph = {i: defaultdict(inf) for i in range(1, n+1)}

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)


res = bellmanford(1)

if not res:
    print(-1)
else:
    for d in res[2:]:
        if d == float('inf'):
            print(-1)
        else:
            print(d)
            
