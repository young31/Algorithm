# tree dp
from collections import defaultdict

def solution(n, wires):
    tree = defaultdict(list)
    for wire in wires:
        a, b = wire
        tree[a].append(b)
        tree[b].append(a)

    def search(cur, used):
        nonlocal hop
        for nxt in tree[cur]:
            if not used[nxt]:
                used[nxt] = True
                if visited[cur][nxt] != False:
                    hop += visited[nxt][cur]
                else:
                    hop += 1
                    search(nxt, used)

    answer = float('inf')
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in tree[i]:
            if visited[i][j] == False:
                used = [False for _ in range(n+1)]
                used[i] = True; used[j] = True
                hop = 1
                search(i, used)

                visited[i][j] = hop
                hop = 1
                search(j, used)
                visited[j][i] = hop

                a = abs(visited[i][j] - visited[j][i])
                answer = min(a, answer)

    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
solution(n, wires)