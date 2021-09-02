def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x]) 
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    if a <= b:
        parents[b] = a
    else:
        parents[a] = b