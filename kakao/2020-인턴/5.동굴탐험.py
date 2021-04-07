# input
n = 9
path = 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]

from collections import deque

def solution(n, path, order):
    N = n
    in_degree = [0 for _ in range(n)]
    undirected_graph = {e: [] for e in range(n)}
    directed_graph = {e: [] for e in range(n)}
    
    for p in path:
        undirected_graph[p[0]].append(p[1])
        undirected_graph[p[1]].append(p[0])

    visited = [False] * n
    visited[0] = True
    q = deque([0])
    while q:
        cur = q.popleft()
        for n in undirected_graph[cur]:
            if visited[n]:
                continue

            visited[n] = True
            q.append(n)
            directed_graph[cur].append(n)
            in_degree[n] += 1

    for o in order:
        directed_graph[o[0]].append(o[1])
        in_degree[o[1]] += 1

    que = deque()
    for i in range(N):
        if in_degree[i] == 0:
            que.append(i)

    while que:
        cur = que.popleft()
        for i in directed_graph[cur]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                que.append(i)

    answer = True if sum(in_degree)==0 else False
    return answer

print(solution(n, path, order))