land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
height = 1
land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
height = 3
from pprint import pprint

from collections import deque
from queue import PriorityQueue

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

def find_parent(parent, x):
    if parent[x] != x: 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def bound_check(visited, i, j):
    n = len(visited)
    if 0 <= i < n and 0 <= j < n: 
        return True
    return False

def solution(land, height):
    answer = 0
    n = len(land)
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    group_n = -1
    connection = {}
    
    for a in range(n):
        for b in range(n):
            if visited[a][b] == -1:
                que = deque([[a, b]])
            else:
                continue
            group_n += 1
            visited[a][b] = group_n
            while que:
                i, j = que.pop()

                for di, dj in moves:
                    ni = i+di
                    nj = j+dj

                    if bound_check(visited, ni, nj):
                        if visited[ni][nj] == -1:
                            if abs(land[i][j] - land[ni][nj]) <= height:
                                que.append((ni, nj))
                                visited[ni][nj] = group_n
                        else:
                            if visited[i][j] != visited[ni][nj]:
                                g1 = visited[i][j]
                                g2 = visited[ni][nj]
                                g1, g2 = set([g1, g2])
                                if g1 not in connection:
                                    connection[g1] = {}
                                if g2 not in connection[g1]:
                                    connection[g1][g2] = int(1e4)

                                connection[g1][g2] = min(connection[g1][g2], abs(land[i][j] - land[ni][nj]))

    graph = []
    parents = [i for i in range(group_n+1)]
    edges = PriorityQueue()
    for a in connection.keys():
        for b in connection[a].keys():
            c = connection[a][b]
            edges.put((c, a, b))

    while edges.qsize() != 0:
        c, a, b = edges.get()
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            answer += c
    print(connection)
    print(visited)
    print(answer)
    return answer

solution(land, height)