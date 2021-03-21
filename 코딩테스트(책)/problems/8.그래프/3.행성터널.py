# input
n = 5
graph = [
    (11, -15, -15), (14, -5, -15), (-1, -1, -5), 
    (10, -4, 1), (19, -4, 19)
]

# answer: 4

# algo
def dist(x, y):
    res = int(1e10)
    for a, b in zip(x, y):
        res = min(res, abs(a-b))
    return res

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

def solution(graph):
    from queue import PriorityQueue
    n = len(graph)
    parents = [i for i in range(n)]
    cost = 0

    edges = PriorityQueue()
    for i in range(n):
        for j in range(i+1, n):
            c = dist(graph[i], graph[j])
            edges.put((c, i, j))

    while edges.qsize() != 0:
        c, a, b = edges.get()
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            cost += c
    print(cost)

solution(graph)
