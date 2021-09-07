import math, heapq

def get_dist(x, y):
    x1, x2 = x
    y1, y2 = y
    res = (x1-y1)**2 + (x2-y2)**2
    return math.sqrt(res)

def prim(start=1):
    visited = [False for _ in range(n+1)]
    dist = []
    heapq.heappush(dist, (0, start, start))
    connected = []
    total_weights = 0

    while dist:
        c, past, cur = heapq.heappop(dist)

        if not visited[cur]:
            visited[cur] = True
            connected.append((past, cur))
            total_weights += c

            for nxt in range(n):
                if not visited[nxt]:
                    cost = graph[cur][nxt]
                    heapq.heappush(dist, (cost, cur, nxt))
    print(round(total_weights, 3))


n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        graph[i][j] = get_dist(stars[i], stars[j])

prim()