import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def count(arr, k):
    return sum(list(map(lambda x: x//k, arr)))

s = 1
e = max(arr)
while s <= e:
    mid = (s+e)//2
    print(s, e, mid)
    if count(arr, mid) >= k:
        s = mid+1
    else:
        e = mid-1

print(s, e)