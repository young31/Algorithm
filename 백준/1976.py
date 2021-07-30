import sys
input = sys.stdin.readline

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

n = int(input())
m = int(input())

parents = list(range(n))
for i in range(n):
    ls = list(map(int, input().split()))
    for j, l in enumerate(ls):
        if l == 1:
            union(parents, i, j)

target = list(map(lambda x: int(x)-1, input().split()))

parent = set()
for tar in target:
    parent.add(find(parents, tar))

if len(parent) == 1:
    print('YES')
else:
    print('NO')