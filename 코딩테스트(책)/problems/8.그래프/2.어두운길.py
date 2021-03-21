# input
n, m = 7, 11
graph = [
    (0, 1, 7), (0, 3, 5), (1, 2, 8), (1, 3, 9), (1, 4, 7), (2, 4, 8),
    (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
]

# answer: 51

# algo
from queue import PriorityQueue
def find(parents, x):
    if parents[x] != x:
        return find(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(graph, n):
    parents = [i for i in range(n)]

    edges = PriorityQueue()
    total_cost = 0
    reduced_cost = 0

    for a, b, c in graph:
        edges.put((c, a, b))
        total_cost += c

    while edges.qsize() != 0:
        c, a, b = edges.get()

        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            reduced_cost += c

    print(total_cost - reduced_cost)
    
solution(graph, n)