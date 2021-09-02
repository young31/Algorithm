# data init
from collections import defaultdict
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


def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

floyd()
for g in graph:
    print(g)
