from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

nodes = [i for i in range(1, n+1)]
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
        SCC.append(sorted(scc))
    
def tarjan():
    for node in nodes:
        if ids[node] == -1:
            dfs(node)

tarjan()
SCC.sort()
print(len(SCC))
for s in SCC:
    tmp = s+[-1]
    print(*tmp)

