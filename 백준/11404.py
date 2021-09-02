from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[float('inf') for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

for g in graph:
    g = [g[i] if g[i] != float('inf') else 0 for i in range(n) ]
    print(*g)