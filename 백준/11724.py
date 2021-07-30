import sys
input = sys.stdin.readline

# 서로소 집합
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

parents = [x for x in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union(parents, a, b)

ans = set()
for i in range(n):
    ans.add(find(parents, i))
print(len(ans))