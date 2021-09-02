from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(list)
in_nodes = {i+1: 0 for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_nodes[b] += 1

que = deque()
visited = [False for _ in range(n+1)]
for k, v in in_nodes.items():
    if v == 0:
        que.append(k)
        visited[k] = True
    
while que:
    cur = que.popleft()
    print(cur, end=' ')
    for k in graph[cur]:
        in_nodes[k] -= 1
        if in_nodes[k] <= 0 and not visited[k]:
            que.append(k)
            visited[k] = True

for i, v in enumerate(visited[1:], 1):
    if not v:
        print(i)
