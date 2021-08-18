from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
for _ in range(N):
    n, m = map(int, input().split())
    nodes = list(range(1, n+1))
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    stack = []

    ids = [-1 for _ in range(n+1)]
    lowlink = [-1 for _ in range(n+1)]
    onStack = [False for _ in range(n+1)]

    groups = {}
    inv_groups = {}
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

            idx = min(scc)
            groups[idx] = scc
            for sc in scc:
                inv_groups[sc] = idx

    # tarjan
    for node in nodes:
        if ids[node] == -1:
            dfs(node)

    # grouping based on scc groups
    group_graph = {}
    for k, vs in groups.items():
        group_graph[k] = set()
        for v in vs:
            for g in graph[v]:
                group_graph[k].add(inv_groups[g])
        group_graph[k] = group_graph[k] - set(vs)
        
    in_nodes = {x:0 for x in group_graph.keys()}
    for k, vs in group_graph.items():
        for v in vs:
            in_nodes[v] += 1
    
    cnt = 0
    for v in in_nodes.values():
        if v == 0:
            cnt += 1
    print(cnt)