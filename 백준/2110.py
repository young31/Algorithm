def search(arr, interval):
    s = arr[0]
    cnt = 1
    for a in arr[1:]:
        if a - s >= interval:
            s = a
            cnt += 1
    return cnt

n, k = map(int, input().split())
arr = [
    int(input()) for _ in range(n)
]

arr.sort()

s = 1
e = arr[-1]

while s <= e:
    mid = (s+e)//2
    cnt = search(arr, mid)
    if cnt >= k:
        s = mid+1
    else:
        e = mid-1

print(e)