a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]

from collections import defaultdict, deque

def solution(a, edges):
    if sum(a) != 0:
        return -1
    answer = 0
    n = len(a)
    scores = defaultdict(int)
    degree = defaultdict(int)
    for i, s in enumerate(a):
        scores[i] = s
        
    graph = defaultdict(deque)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
        degree[i] += 1
        degree[j] += 1

    que = deque([])
    for k, v in degree.items():
        if v == 1:
            que.append(k)

    while que:
        child = que.popleft()
        if not graph[child]:
            continue
        parent = graph[child][0]
        
        degree[parent] -= 1
        if degree[parent] == 1:
            que.append(parent)
        graph[parent].remove(child)

        scores[parent] += scores[child]
        answer += abs(scores[child])
        scores[child] = 0

    return answer

solution(a, edges)