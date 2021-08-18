from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def is_possible(m):
    que = deque([A])
    visited = [False for _ in range(n+1)]
    visited[A] = True
    max_ = 0
    while que:
        cur = que.pop()
        if cur == B:
            return True, max_
        for nxt in graph[cur].keys():
            if not visited[nxt] and graph[cur][nxt] > m:
                max_ = max(graph[cur][nxt], max_)
                que.append(nxt)
                visited[nxt] = True
    return False, max_
    

n, m = map(int, input().split())
graph = defaultdict(dict)

r = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if b not in graph[a].keys():
        graph[a][b] = 0
    if a not in graph[b].keys():
        graph[b][a] = 0
    graph[a][b] = max(c, graph[a][b])
    graph[b][a] = max(c, graph[b][a])
    r = max(r, c)

A, B = map(int, input().split())

l = 1
r += 1
while l <= r:
    mid = (l+r)//2
    p, m = is_possible(mid)
    if p:
        l = mid+1
    else:
        r = mid-1

print(l)