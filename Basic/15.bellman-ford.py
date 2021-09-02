# 음의 가중치가 있을 때 음수 사이클이 있는지 확인하는 알고리즘
## n-1번 가중치 업데이트하고 또 업데이트 할 때 가중치가 변하면 사이클!
## 이 과정에서 노드사이의 최소 거리를 구하게 되어 사용함
## 백준 11657 1738 1865 10360 1219 
n = 3
graph = { # dict( dict() ) 형태
    0: {1: 4, 2: 3},
    1: {2: -1},
    2: {0: -2}
} 
def bellmanford(start):
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    # 최소거리 계산
    for rep in range(1, n+1): # n-1 번
        for node in graph.keys(): # 모든 노드에 대해서 
            for adj, d in graph[node].items():
                if dist[node] + d < dist[adj]:
                    dist[adj] = dist[node] + d
                    if rep == n:
                        return False

    return dist

print(bellmanford(0))


