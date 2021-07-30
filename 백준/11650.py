import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()
for a in arr:
    print(*a)