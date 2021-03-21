# input
n, m = 5, 4
graph = [
    [0, 1, 0, 1, 1], 
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0]
]
path = [2, 3, 4, 3]

# answer: YES

# algo
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

def solution(graph, path):
    n = len(graph)
    parents = [i for i in range(n+1)]

    for i in range(n):
        for j in range(n):
            union(parents, i+1, j+1)

    # 모두 같은 부모면 연결되어 있음
    res = True
    parent = parents[path[0]]
    for p in path:
        res *= (parents[p] == parent) # 하나라도 다르면 0이됨
    
    if res == 1:
        return 'YES'
    else:
        return 'NO'
    

solution(graph, path)


