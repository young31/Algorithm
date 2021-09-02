# 순서가 있는 작업의 처리
# 사이클이 없는 방향그래프에 적용

# data init
edges = [
    (1, 2), (1, 5), (2, 3), (5, 6), (3, 4), (4, 6), (6, 7)
]

nodes = list(range(1, 8))

from collections import defaultdict, deque
graph = defaultdict(list)
in_nodes = defaultdict(int)

for edge in edges:
    graph[edge[0]].append(edge[1])
    in_nodes[edge[1]] += 1 # 진입 차수 계산

que = deque()
for node in nodes:
    if in_nodes[node] == 0:
        que.append(node)

while que:
    cur = que.popleft()
    print(cur)
    for node in graph[cur]: 
        in_nodes[node] -= 1 # 전 단계를 방문하니까 진입차수 -1
        if in_nodes[node] == 0: # 진입차수가 0이면 들어갈 수 있으니 들어가 줌
            que.append(node)

