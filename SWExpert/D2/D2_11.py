# young 127ms, 427
T = int(input())
 
for i in range(1,T+1):
    x1, x2 = map(int, input().split( ))
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    if x1 >= x2:
        a = a1
        b = a2
    else:
        a = a2
        b = a1
 
    c = []
    for k in range(0, abs(x1-x2)+1) :
        t = 0
        for j in range(0,len(b)) :
            t += b[j] * a[k+j]
        c.append(t)
    print('#%d'%i, max(c))