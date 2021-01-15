# input
n, m = 6, 11
start = 1
inf = int(float(1e10))
distance = [inf for _ in range(n+1)]
visited = [False for _ in range(n+1)]
# 딕셔너리가 편해서 사용했지만 일반적으로 리스트를 사용
graph = {
    1: {
        2: 2, 3: 5, 4: 1
    },
    2: {
        3: 3, 4: 2,
    },
    3: {
        2: 3, 6: 5
    },
    4: {
        3: 3, 5: 1
    },
    5: {
        3: 1, 6: 2
    }
}
# answer: 

# algo
# 계속해서 작은 값부터 초기화해서 제일 짧은 길을 더해가기 위해서
def get_smallest_node():
    index = 0
    min_ = inf
    for i in range(1, n+1):
        if distance[i] < min_ and not visited[i]:
            min_ = distance[i]
            index = i
    return index

def dijkstra1(start):
    # initialize
    distance[start] = 0
    visited[start] = True
    for k, v in graph[start].items():
        distance[k] = v
    for _ in range(n-1):
        cur = get_smallest_node()
        visited[cur] = True
        if cur in graph.keys():
            for k, v in graph[cur].items():
                cost = v + distance[cur]
                if cost < distance[k]:
                    distance[k] = cost


def dijkstra2(start): # smallest node를 찾는 과정을 단축시킴
    import heapq
    distance[start] = 0
    visited[start] = True
    q = [] # 차이점
    heapq.heappush(q, (0, start))
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

dijkstra2(start)
print(distance)