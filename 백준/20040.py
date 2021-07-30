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

n, m = map(int, input().split())
parents = list(range(n))
done = False
for c in range(m):
    a, b = map(int, input().split())
    if find(parents, a) == find(parents, b):
        print(c+1)
        done = True
        break
    else:
        union(parents, a, b)

if not done:
    print(0)