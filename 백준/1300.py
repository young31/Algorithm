def count(n, k):
    cnt = 0
    for i in range(1, n+1):
        
        if k//i == 0:
            return cnt
        else:
            cnt += min(k//i, n)
    return cnt

n = int(input())
m = int(input())

s = 1
e = n*n

while s <= e:
    mid = (s+e)//2
    cnt = count(n, mid)
    if cnt >= m:
        e = mid-1
    else:
        s = mid+1

print(e)
