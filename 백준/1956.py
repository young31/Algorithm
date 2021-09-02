import heapq
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

m = float('inf')
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] != float('inf') and graph[j][i] != float('inf'):
            print(i, j)
            m = min(m, graph[i][j]+graph[j][i])

from pprint import pprint
pprint(graph)
if m == float('inf'):
    print(-1)
else:
    print(m)