from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def inf(): return float('inf')
graph = {i: defaultdict(inf) for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n+1):
    graph[i][i] = 0

hist = {i: [[i] for j in range(n)] for i in range(1, n+1)}

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cur = graph[i][j]
            new = graph[i][k] + graph[k][j]
            if new < cur:
                graph[i][j] = new
                hist[i][j-1] = hist[i][k-1] + hist[k][j-1]

for i in range(1, n+1):
    g = graph[i]
    for j in range(1, n+1):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()

for i in range(1, n+1):
    h = hist[i]
    for j in range(n):
        if graph[i][j+1] == 0:
            print(0)
        else:
            print(len(h[j])+1, end=' ')
            print(*(h[j]+[j+1]))