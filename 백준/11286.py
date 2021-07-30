import heapq
import sys 
input = sys.stdin.readline

n = int(input())

que = []
for _ in range(n):
    k = int(input())
    if k == 0:
        if len(que) == 0:
            print(0)
        else:
            _, q = heapq.heappop(que)
            print(q)
    else:
        heapq.heappush(que, (abs(k), k))