import heapq

n = int(input())

visited = [False for _ in range(n)]
mat = [list(map(int, input().split())) for _ in range(n)]

que = [(
    0, 0, visited
)]

while que:
    c, x, v = heapq.heappop(que)
    if sum(v) == n and x == 0:
        print(c)
        break
    for i, nxt in enumerate(mat[x]):
        if nxt != 0 and not v[i]:
            tmp = v.copy()
            tmp[i] = True
            heapq.heappush(que, (c+nxt, i, tmp))