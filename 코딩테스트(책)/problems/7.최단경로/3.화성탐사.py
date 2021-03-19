# input
n1 = 3
graph1 = [
    [5, 5, 4],
    [3, 9, 1],
    [3, 2, 7]
]

n2 = 5
graph2 = [
    [3, 7, 2, 0, 1], [2, 8, 0, 9, 1], [1, 2, 1, 8, 1], [9, 8, 9, 2, 0], [3, 6, 5, 1, 5]
]

n3 = 7
graph3 = [
    [9, 0, 5, 1, 1, 5, 3], [4, 1, 2, 1, 6, 5, 3], [0, 7, 6, 1, 6, 8, 5],
    [1, 1, 7, 8, 3, 2, 3], [9, 4, 0, 7, 6, 4, 1], [5, 8, 3, 2, 4, 8, 3],
    [7, 4, 8, 4, 8, 3, 4]
]
# answer: 20

# algo
import heapq

moves =[
    (0, 1), (0, -1), (1, 0), (-1, 0)
]
def solution(graph):
    n = len(graph)
    inf = int(1e9)
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[inf for _ in range(n)] for _ in range(n)]

    q = []
    heapq.heappush(q, (0, 0, 0))
    while q:
        c, x, y = heapq.heappop(q)

        for dx, dy in moves:
            if 0 <= x+dx < n and 0 <= y+dy < n:
                n_cost = c + graph[x][y]
                if distance[x+dx][y+dy] > n_cost:
                    distance[x+dx][y+dy] = n_cost
                    heapq.heappush(q, (n_cost, x+dx, y+dy))
        
    print(distance[n-1][n-1] + graph[n-1][n-1])




solution(graph1)
solution(graph2)
solution(graph3)