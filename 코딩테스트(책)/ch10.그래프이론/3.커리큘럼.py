# input
n = 5
inputs = [
    (10, -1), (10, 1, -1), (4, 1, -1), (4, 3, 1, -1), (3, 3, -1)
]

# answer: 10, 20, 14, 18, 17

# algo
from collections import deque
from copy import deepcopy

def main():
    # 위상정렬
    in_degree = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    time = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        time[i] = inputs[i-1][0]
        if len(inputs[i-1]) > 2:
            ls = inputs[i-1][1:-1]
            for j in ls:
                graph[j].append(i)
                in_degree[i] += 1
    
    res = deepcopy(time)
    que = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            que.append(i)

    while que:
        cur = que.popleft()

        for i in graph[cur]:
            res[i] = max(res[i], res[cur]+time[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                que.append(i)
    print(res)

def main2():
    # DP방식으로 풀어보려고 했음
    ## 큰 차이가 없어보임
    graph = [[] for _ in range(n+1)]
    time = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        time[i] = inputs[i-1][0]
        if len(inputs[i-1]) > 2:
            ls = inputs[i-1][1:-1]
            for j in ls:
                graph[j].append(i)
    
    res = deepcopy(time)

    for i, g in enumerate(graph[1:], 1):
        for k in g:
            res[k] = max(res[k], time[k]+res[i])

    print(res)

main()
main2()
        