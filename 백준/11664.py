# 수치해석
import math

def interpolate(s, e, f, n=1e6):
    return [s[i] + (e[i]-s[i])*f/n for i in range(3)]

def dist(a, b):
    res = [(a[i]-b[i])**2 for i in range(3)]
    return sum(res)


cord = list(map(int, input().split()))

a = cord[:3]
b = cord[3:6]
c = cord[6:]

s = 0
e = 1e6
m = float('inf')
while s <= e:
    mid = (s+e)//2
    new = interpolate(a, b, mid)
    s_cord = interpolate(a, b, s)
    e_cord = interpolate(a, b, e)
    dn = dist(new, c)
    if dn < m:
        m = dn
    
    ds = dist(c, s_cord)
    de = dist(c, e_cord)

    if ds < de:
        e = mid-1
    else:
        s = mid+1

print(math.sqrt(m))




