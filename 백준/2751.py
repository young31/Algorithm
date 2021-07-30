import heapq
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

while arr:
    print(heapq.heappop(arr))