# input
v, e = 7, 8
graph = [
    (1, 2), (1, 5), (2, 3), (2, 6), (3, 4), (4, 7), (5, 6), (6, 4)
]
# answer: 1, 2, 5, 3, 6, 4, 7

# algo
## *방향그래프* 에서 진입조건을 고려한 정렬
## 진압차수가 0인 노드를 큐에 넣는다.
## 큐를 돌면서 해당 노드에서 나가는 간선을 제거한다.
## 큐에 들어갔던 순서가 정렬!

def main():
    from collections import deque
    g = [[] for _ in range(v+1)]
    inDegree = [0 for _ in range(v+1)]

    for a, b in graph:
        g[a].append(b)
        inDegree[b] += 1

    res = []
    que = deque()

    for i in range(1, v+1):
        if inDegree[i] == 0:
            que.append(i)

    while que:
        cur = que.popleft()
        res.append(cur)

        for i in g[cur]:
            inDegree[i] -= 1
            if inDegree[i] == 0:
                que.append(i)

    print(res)

def main2():
    # 몰랐다면 풀었을 방식
    from collections import deque

    inDct = {}
    outDct = {}
    res = []

    for i in range(1, v+1):
        inDct[i] = []
        outDct[i] = []

    for a, b in graph:
        inDct[a].append(b)
        outDct[b].append(a)

    que = deque()
    for k in outDct.keys():
        if len(outDct[k]) == 0:
            que.append(k)
            

    while que:
        cur = que.popleft()
        res.append(cur)

        for i in inDct[cur]:
            outDct[i].remove(cur)
            if len(outDct[i]) == 0:
                que.append(i)
            
    print(res)
    
main()
main2()