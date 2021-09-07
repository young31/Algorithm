# solution 1
## cycle 찾을 때 하나하나 찾으면 시간초과에 걸린다
## 역방향 간선이라는 것을 찾는 방식으로 구현하여야 한다.
from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**9-1)

# def is_cycle(graph, start, visited):
#     que = deque([start])
#     visited[start] = True
#     while que:
#         cur = que.pop()
#         for v in graph[cur]:
#             if v == start:
#                 return True
#             if not visited[v]:
#                 que.append(v)
#                 visited[v] = True
#     return False
def solution(n, path, order):
    def is_cycle(start):
        nonlocal visited, iscycle, finished
        visited[start] = True
        for v in dg[start]:
            if not visited[v]:
                is_cycle(v)
            elif not finished[v]:
                iscycle = True
        finished[start] = True

    p2c = defaultdict(set)
    for p, c in path:
        p2c[p].add(c)
        p2c[c].add(p)

    visited = [False for _ in range(n)]
    dg = defaultdict(list)
    start = 0
    que = deque([start])
    while que:
        i = que.popleft()
        visited[i] = True
        vs = p2c[i]
        for v in vs:
            if not visited[v]:
                dg[v].append(i)
                que.append(v)
        
    for op, oc in order:
        dg[oc].append(op)

    visited = [False for _ in range(n)]
    finished = [False for _ in range(n)]
    iscycle = False
    for i in range(n):
        is_cycle(i)
        if iscycle:
            return False
    return True
        
# solution 2
## 푸는 방식을 모르고 논리만 이용해서 푼 방법
## 시간은 어째 이게 더 빠르다..
from collections import deque

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    vis = [False] * n
    for p in path:
        graph[p[0]] += [p[1]]
        graph[p[1]] += [p[0]]
    fromto = dict()
    tofrom = dict()
    for o in order:
        fromto[o[0]] = o[1]  # key가 선행노드
        tofrom[o[1]] = o[0]  # key가 후행노드
    path = [False] * n

    def bfs():
        Q = deque([0])
        vis[0] = True
        while Q:
            curr = Q.popleft()
            path[curr] = True
            if tofrom.get(curr) is None:
                vis[curr] = True
                for nxt in graph[curr]:
                    if vis[nxt] == False:
                        Q.append(nxt)
                if fromto.get(curr) is not None and path[fromto[curr]] == True:  # jump
                    Q.append(fromto[curr])
            else:
                if vis[tofrom[curr]] == True:
                    vis[curr] = True
                    for nxt in graph[curr]:
                        if vis[nxt] == False:
                            Q.append(nxt)

    bfs()
    if False in path:
        return False
    else:
        return True

# solution 3
## 순서에 맞춰서 들어갈 수 있는 노드 숫자를 계산해서 해결
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