n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def find(parent, x):
    if parent[x] != x: 
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, computers):
    answer = 0
    parents = [i for i in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                union(parents, i, j)
    print(parents)
    for i in range(n):
        parents[i] = find(parents, i)
    answer = len(set(parents))
    return answer

solution(n, computers)