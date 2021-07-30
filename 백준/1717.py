import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

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

n, m = map(int, input().split())

parents = [x for x in range(n+1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(parents, a, b)
    else:
        ap = find(parents, a)
        bp = find(parents, b)
        if ap == bp:
            print('YES')
        else:
            print('NO')

