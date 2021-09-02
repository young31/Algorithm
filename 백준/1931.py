import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(arr, (b, a))

answer = 0
cur_e = cur_s = 0
for _ in range(n):
    e, s = heapq.heappop(arr)
    if s >= cur_e:
        answer += 1
        cur_s = s
        cur_e = e

print(answer)