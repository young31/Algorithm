import sys
input = sys.stdin.readline

N = int(input())
arr = set()
for _ in range(N):
    s = input().strip()
    arr.add((len(s), s))

arr = list(arr)
arr.sort()
for a in arr:
    print(a[1])