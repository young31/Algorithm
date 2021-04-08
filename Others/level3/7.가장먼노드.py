n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


import heapq

def solution(n, edge):
    inf = int(1e6)
    graph = {e: {e: 1} for e in range(n)}
    for a, b in edge:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1
    graph_ = graph.copy()

    
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    distance[0] = 0
    visited[0] = True
    q = [] 
    heapq.heappush(q, (0, 0))
    
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        if cur in graph.keys():
            for k, v in graph[cur].items():
                cost = dist + v
                if cost < distance[k]:
                    distance[k] = cost
                    heapq.heappush(q, (cost, k))

    dist = max(distance)
    answer = distance.count(dist)
    return answer

solution(n, edge)