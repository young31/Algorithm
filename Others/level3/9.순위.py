n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

from collections import deque

def find(graph, x, n):
    que = deque([x])
    visited = [False]*(n+1)
    visited[x] = True
    while que:
        cur = que.popleft()

        for g in graph[cur]:
            if not visited[g]:
                visited[g] = True
                que.append(g)

    return sum(visited)-1

def solution(n, results):
    answer = 0
    con_in = {e:[] for e in range(1, n+1)}
    con_out = {e:[] for e in range(1, n+1)}
    for a, b in results:
        con_in[a].append(b)
        con_out[b].append(a)

    print(con_in, con_out)
    for i in range(1, n+1):
        n_in = find(con_in, i, n)
        n_out = find(con_out, i, n)
        print(i, n_in, n_out)
        if n_in+n_out == n-1:
            answer+=1
    print(answer)
    return answer

solution(n, results)