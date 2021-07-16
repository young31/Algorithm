# input
n, m, C = 3, 2, 1
graph = {
    1: {2: 4, 3: 2}
}
# answer: 2, 4

# algo
inf = int(1e10)
graph_ = graph.copy()
for i in range(1, n+1): 
    if i in graph.keys():
        graph[i][i] = 0
    else:
        graph[i] = {}
        graph[i][i] = 0

i = 1
for j in range(1, n+1):
    for k in range(1, n+1):
        a = graph[i][k] if k in graph[i].keys() else inf
        b = graph[k][j] if j in graph[k].keys() else inf
        c = graph[i][j] if j in graph[i].keys() else inf
        graph_[i][j] = min(c, a+b)

cnt = 0
maxDur = -1
for k in graph_.keys(): 
    for i, v in graph_[k].items():
        if v != inf and i != C:
            cnt += 1
            if maxDur < v:
                maxDur = v
print(cnt, maxDur)
