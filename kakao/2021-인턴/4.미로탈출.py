# 실패
from collections import defaultdict
import heapq
def inf(): return float('inf')

def solution(n, start, end, roads, traps):
    visited = [
        [False for _ in range(n+1)] for _ in range(2)
    ]
    graph = [{i: defaultdict(inf) for i in range(1, n+1)} for _ in range(2)]

    for p, q, s in roads:
        graph[0][p][q] = min(graph[0][p][q], s)
        graph[1][q][p] = min(graph[1][q][p], s)

    # dist의 양 / 음의 방향에서 들어온 것을 구분
    # dijkstra
    # 둘 중 작은 값을 출력
    dist = [[float('inf') for _ in range(n+1)] for _ in range(2)]
    # phases = [0 for _ in range(n+1)]
    que = [(0, start, 0, 0)] # cost node phase
    while que:
        c, cur, node_phase, edge_phase = heapq.heappop(que)
        print(c, cur, node_phase, edge_phase)
        if dist[edge_phase][cur] < c:
            continue
        if cur in traps:
            edge_nxt = 1 - edge_phase
        else:
            edge_nxt = edge_phase

        for nxt, c_nxt in graph[edge_phase][cur].items():
            if nxt in traps:
                phase_nxt = 1 - node_phase
            c_new = c_nxt + c
            if c_new < dist[edge_phase][nxt]:
                dist[edge_phase][nxt] = c_new
                heapq.heappush(que, (c_new, nxt, phase_nxt, edge_nxt))

    print(dist)
    answer = min(dist[0][end], dist[1][end])
    print(answer)
    return answer


n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
solution(n, start, end, roads, traps)

[[0 for _ in range(1000)] for _ in range(1000)]