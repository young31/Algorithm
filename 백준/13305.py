import heapq
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

price_sort = []
for i, p in enumerate(price[:-1]):
    heapq.heappush(price_sort, (p, i))

answer = 0
end = len(dist)

for _ in range(n-1):
    p, i = heapq.heappop(price_sort)
    if i == 0:
        answer += sum(dist[i:end])*p
        break
    if i < end:
        answer += sum(dist[i:end])*p
        end = i

print(answer)