n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = 1
c = arr[s] + arr[e]
ans = float('inf')
while s <= e:
    if c >= k:
        print(c, s, e)
        ans = min(e-s+1, ans)
        c -= arr[s]
        s += 1
    else:
        if e == n-1:
            break
        else:
            e += 1
            c += arr[e]

if ans == float('inf'):
    ans = 0
print(ans)