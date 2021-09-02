# 방향 그래프에서 연결가능한 집합으로 구분
## 응용처는 좀 더 공부해야 할 듯
## 백준: 2150, 4196, 3977

# data init
nodes = list(range(1, 8))
n = len(nodes)
edges = [
    (1, 4), (4, 5), (5, 1), (1, 6), (6, 7), 
    (2, 7), (7, 3), (3, 7), (7, 2)
]
from collections import defaultdict
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)

# tarjan
stack = []
SCC = []

ids = [-1 for _ in range(n+1)]
lowlink = [-1 for _ in range(n+1)]
onStack = [False for _ in range(n+1)]

k = 0
def dfs(node):
    global k
    onStack[node] = True
    stack.append(node)
    ids[node] = k
    lowlink[node] = k
    k += 1
    for adj in graph[node]:
        if ids[adj] == -1:
            dfs(adj)
            lowlink[node] = min(lowlink[node], lowlink[adj])
        elif onStack[adj]:
            lowlink[node] = min(lowlink[node], ids[adj])

    if lowlink[node] == ids[node]:
        scc = []
        while 1:
            t = stack.pop()
            scc.append(t)
            onStack[t] = False
            if t == node:
                break
        SCC.append(scc)
    
def tarjan():
    for node in nodes:
        if ids[node] == -1:
            dfs(node)
    print(SCC)
tarjan()
            
# kosaraju
## 구현이 더 직관적이고 쉬움

## 정방향 dfs로 모든 정점을 stack에
def dfs(node, stack):
    visited[node] = True
    for adj in graph[node]:
        if not visited[adj]:
            stack.append(adj)
            dfs(adj, stack)
    stack.append(node)

## 역방향으로 빼면서 scc에 포함
def rev_dfs(node, stack):
    visited[node] = True
    stack.append(node)
    for adj in rev_graph[node]:
        if not visited[adj]:
            rev_dfs(adj, stack)

## 역방향 그래프 생성
rev_graph = defaultdict(list)
for k, vs in graph.items():
    for v in vs:
        rev_graph[v].append(k)

## 정방향 dfs
stack = []
visited = [False for _ in range(n+1)]
for node in nodes:
    if not visited[node]:
        dfs(node, stack)
print(stack)

## 역방향 dfs
visited = [False for _ in range(n+1)]
res = []
while stack:
    t = stack.pop()
    if not visited[t]:
        scc = []
        rev_dfs(t, scc)
        res.append(scc)
print(res)
