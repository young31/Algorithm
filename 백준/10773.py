import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if arr:
            arr.pop()
    else:
        arr.append(a)

print(sum(arr))