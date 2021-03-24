# input
map1 = [
    [0, 0, 0], [0, 0, 0], [0, 9, 0]
]

map2 = [
    [0, 0, 1], [0, 0, 0], [0, 9, 0]
]

map3 = [
    [4, 3, 2, 1], [0, 0, 0, 0], [0, 0, 9, 0], [1, 2, 3, 4]
]
# answer: 0, 3, 14

# algo
from collections import deque
from pprint import pprint
import heapq

class Baby:
    def __init__(self, start):
        self.loc = start
        self.size = 2
        self.eat = 0
        self.n_move = 0

    def move(self, dest, distance):
        self.loc = dest
        self.eat += 1
        self.n_move += distance
        if self.eat == self.size:
            self.eat = 0
            self.size += 1

def is_feasible(graph, x, y, size):
    n = len(graph)
    if 0 <= x < n and 0 <= y < n and graph[x][y] <= size:
        return True
    return False

def compute_dist(graph, start, size):
    moves = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]

    que = deque()
    n = len(graph)
    visited = [[False for _ in range(n)] for _ in range(n)]
    que.append(start+(0,))
    opt = -1
    candidates = []
    visited[start[0]][start[1]] = True
    while que:
        x, y, c = que.popleft()
        if c == opt:
            return sorted(candidates)[0], opt
        
        for dx, dy in moves:
            if is_feasible(graph, x+dx, y+dy, size-1) and graph[x+dx][y+dy] != 0:
                opt = c+1
                candidates.append((x+dx, y+dy))
            if is_feasible(graph, x+dx, y+dy, size) and not visited[x+dx][y+dy]:
                que.append((x+dx, y+dy, c+1))
                visited[x+dx][y+dy] = True

    return False, 0
 
def solution(graph):
    for i, g in enumerate(graph):
        for j in range(len(g)):
            if g[j] == 9:
                cur = (i, j)
                g[j] = 0

    shark = Baby(cur)
    while 1:
        best, distance = compute_dist(graph, shark.loc, shark.size)
        if not best:
            print(shark.n_move)
            return 
        shark.move(best, distance)
        graph[best[0]][best[1]] = 0

solution(map1)
solution(map2)
solution(map3)


