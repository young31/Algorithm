# input
n, m = 4, 7
graph = {
    1: {2: 4, 4: 6},
    2: {1: 3, 3: 7},
    3: {1: 5, 4: 4},
    4: {3: 2}
}
# answer: 
[
    [0, 4, 8, 6],
    [3, 0, 7, 9],
    [5, 9, 0, 4],
    [7, 11, 2, 0]
]
# algo
inf = int(1e10)
graph_ = graph.copy()
for i in graph_.keys(): graph_[i][i] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            a = graph[i][k] if k in graph[i].keys() else inf
            b = graph[k][j] if j in graph[k].keys() else inf
            c = graph[i][j] if j in graph[i].keys() else inf
            graph_[i][j] = min(c, a+b)

for k in graph_.keys(): print(graph_[k])

### list version
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
