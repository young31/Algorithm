# input
n, m = 6, 6
compare = [
    [1, 5], [3, 4], [4, 2], [4, 6], [5, 2], [5, 4]
]

# answer: 1

# algo
# 낮은 쪽 학생의 수와 높은 쪽 학생의 수의 합이 전체이면 확인가능
## 플로이드 와샬로 도달 가능 여부만 확인하는 방식도 가능함
from collections import deque

def search(graph, student):
    n = len(graph)
    que = deque(graph[student])
    visited = [False for _ in range(n+1)]

    while que:
        nxt = que.popleft()
        visited[nxt] = True

        for s in graph[nxt]:
            que.append(s)

    return sum(visited)

students = list(range(1, n+1))
graph = {}
inv_graph = {}

for i in range(1, n+1):
    graph[i] = []
    inv_graph[i] = []

for a, b in compare:
    graph[a].append(b)
    inv_graph[b].append(a)

cnt = 0
for s in students:
    connected = search(graph, s) + search(inv_graph, s)
    if connected == n-1:
        cnt += 1

print(cnt)

    