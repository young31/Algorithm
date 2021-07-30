from collections import defaultdict, deque
import sys
input = sys.stdin.readline

graph = defaultdict(set)

n = int(input())

visited = [False for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

perm = list(map(int, input().split()))

que = deque([1])
visited[1] = True

idx = 1
ans = 1
used = set([1])
while que:
    c = que.popleft()
    len_ = len(graph[c]-used)

    if graph[c]-used != set(perm[idx:idx+len_]):
        ans = 0
        break
    else:
        for i in range(idx, idx+len_):
            if not visited[perm[i]]: 
                que.append(perm[i])
                used.add(perm[i])
        idx += len_

print(ans)

