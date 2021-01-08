# young 157ms, 186
T = int(input())
 
for i in range(1,T+1) :
    t = int(input())
    s = set()
    n = 1
    while len(s) < 10 :
        s.update(list(str(n*t)))
        n += 1
    print('#%d'%i, (n-1)*t)