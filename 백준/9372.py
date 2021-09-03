import heapq
import sys
input = sys.stdin.readline

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

N = int(input())

for _ in range(N):
    n, m = map(int, input().split())

    parents = [i for i in range(n+1)]
    graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        c = 1
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
        heapq.heappush(edges, (c, a, b))
        heapq.heappush(edges, (c, b, a))

    connected = []
    while edges:
        cost, a, b = heapq.heappop(edges) # 작은 것을 뽑아서
        if find(parents, a) != find(parents, b): # 사이클이 없으면 해당 edge 선택
            connected.append((a, b))
            union(parents, a, b)

    print(len(connected))