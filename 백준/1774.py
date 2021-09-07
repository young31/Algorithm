import math, heapq

def get_dist(x, y):
    x1, x2 = x
    y1, y2 = y
    res = (x1-y1)**2 + (x2-y2)**2
    return math.sqrt(res)

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

def kruskal():
    total_cost = 0.
    while edges:
        cost, a, b = heapq.heappop(edges) # 작은 것을 뽑아서
        if find(parents, a) != find(parents, b): # 사이클이 없으면 해당 edge 선택
            total_cost += cost
            union(parents, a, b)

    print(f'{total_cost:.2f}')

n, m = map(int, input().split())
loc = [list(map(float, input().split())) for _ in range(n)]
parents = [i for i in range(n+1)]
edges = []
for i in range(n):
    for j in range(n):
        if i != j:
            a = loc[i]; b = loc[j]
            heapq.heappush(edges, (get_dist(a, b), i+1, j+1))

for _ in range(m):
    a, b = map(int, input().split())
    union(parents, a, b)

kruskal()