# 최소비용으로 모든 노드 연결(최소 비용 신장 트리)
## 비용 작은 것 부터 추가 시키면서 사이클 여부만 확인
## 사이클 확인은 union - find로 판단

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x]) 
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    if a <= b:
        parents[b] = a
    else:
        parents[a] = b

def kruskal(graph, n):
    import heapq
    parents = [i for i in range(n+2)]

    # 비용이 작은 순서부터 뽑기
    edges = []
    for k, es in graph.items():
        for e in es:
            heapq.heappush(edges, (e[0], e[1], k))

    total_cost = 0
    connected = []
    while edges:
        cost, a, b = heapq.heappop(edges) # 작은 것을 뽑아서
        if find(parents, a) != find(parents, b): # 사이클이 없으면 해당 edge 선택
            connected.append((a, b))
            total_cost += cost
            union(parents, a, b)

    print(connected)
    print(total_cost)

graph = {
    1: [(67, 2), (28, 4), (17, 5), (12, 7)],
    2: [(67, 1), (24, 4), (62, 5)],
    3: [(20, 5), (37, 6)],
    4: [(28, 1), (24, 2), (13, 7)],
    5: [(45, 6), (73, 7)],
}

kruskal(graph, 7)

