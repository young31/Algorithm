from collections import deque

graph = [ # 인접 리스트형태 // dict로도 구현 가능
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 재귀로 구현
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 큐로 구현
def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = True
    while len(q) != 0:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


print('start dfs')
visited = [False for _ in range(9)] # 노드 수
dfs(graph, 1, visited)

print('\nstart bfs')
visited = [False for _ in range(9)] # 노드 수
bfs(graph, 1, visited)