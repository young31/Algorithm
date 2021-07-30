import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

items = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(items, (a, b))

for _ in range(k):
    heapq.heappush(items, (int(input()), 1000001))

cnt = 0
ans = 0
sub = []

while items:
    a, b = heapq.heappop(items)
    if b != 1000001:
        heapq.heappush(sub, (-b, a))
    else:
        if sub:
            v, m = heapq.heappop(sub)
            ans -= v
        cnt += 1

    if cnt == k:
        break
print(ans)