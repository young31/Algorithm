from queue import PriorityQueue

def find(parent, x):
    if parent[x] != x: 
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    parents = [i for i in range(n)]
    answer = 0
    edges = PriorityQueue()
    for a, b, c in costs:
        edges.put((c, a, b))
        
    while edges.qsize() != 0:
        c, a, b = edges.get()
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            answer += c
            
    return answer