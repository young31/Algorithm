n = int(input())
arr = list(map(int, input().split()))

arr.sort()
score = float('inf')
ans = [0, 0]
s = 0
e = n-1

while s != e:
    m = arr[s] + arr[e]
    
    if abs(m) < abs(score):
        ans[0] = arr[s]
        ans[1] = arr[e]
        score = abs(m)
    
    if m == 0:
        break
    elif m > 0:
        e -= 1
    else:
        s += 1
print(*ans)
