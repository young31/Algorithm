from copy import deepcopy
from collections import defaultdict
import sys
input = sys.stdin.readline

def search(i, c=0):
    global ans, visited
    if ans:
        return
    if c == 4:
        if not ans:
            ans = True
            print(1)
        return
    else:
        for j in graph[i]:
            if not visited[j]:
                visited[j] = True
                search(j, c+1)
                visited[j] = False

n, m = map(int, input().split())

# 그래프 구조가 핵심
graph = defaultdict(list)

for _ in  range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = False
for i in range(n):
    if not ans:
        visited = [False for _ in range(n)]
        visited[i] = True
        search(i)
if not ans:
    print(0)