def criterion(m):
    return m * c * ((1 / ((a**2 - m**2)**0.5)) + (1 / ((b**2 - m**2)**0.5)))

a, b, c = map(float, input().split())

s = 0
e = min(a, b)

while s <= e:
    mid = (s+e)/2
    k = criterion(mid)
    if k >= mid:
        e = mid-0.0001
    else:
        s = mid+0.0001

print(s)
