# input
n1 = 5
past1 = [5, 4, 3, 2, 1]
m1 = 2
new1=  [(2, 4), (3, 4)]

n2 = 3
past2 = [2, 3, 1]
m2 = 0
new2 = []

n3 = 4
past3 = [1, 2, 3, 4]
m3 = 3
new3 = [(1, 2), (3, 4), (2, 3)]
# answer: 5, 3, 2, 4, 1 // 2, 3, 1 // IMPOSSIBLE

# algo
from collections import deque

def solution(past, new):
    graph = {}
    inv_graph = {i: [] for i in past}
    n = len(past)
    for i, p in enumerate(past):
        graph[p] = past[:i]
        inv_graph[p] = past[i+1:]

    # 제출되는 정보는 이겼다는 정보가 아니라 역전되었다는 정보임!
    for a, b in new:
        if b in graph[a]:
            graph[a].remove(b)
            inv_graph[a].append(b)
            graph[b].append(a)
            inv_graph[b].remove(a)
        else:
            graph[a].append(b)
            inv_graph[a].remove(b)
            graph[b].remove(a)
            inv_graph[b].append(a)


    in_degree = {i: len(graph[i]) for i in past}    

    que = deque()
    res = []

    for _ in range(n):
        for k in graph.keys():
            if in_degree[k] == 0:
                que.append(k)
                res.append(k)
                
        if len(que) >= 2:
            print('?')
            return 
        elif len(que) == 0:
            print('IMPOSSIBLE')
            return

        rm = que.popleft()
        graph.pop(rm)
        target = inv_graph[rm]

        for kk in target:
            in_degree[kk] -= 1
            graph[kk].remove(rm)

    for r in res: print(r, end=' ')
    print()
    return

solution(past1, new1)
solution(past2, new2)
solution(past3, new3)