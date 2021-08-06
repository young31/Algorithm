def count(arr, cut):
    tmp = list(filter(lambda x: x >= cut, arr))
    return sum(tmp) - cut*len(tmp)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = max(arr)

while s < e:
    mid = (s+e)//2
    if count(arr, mid) >= k:
        s = mid+1
    else:
        e = mid-1

print(s-1)
