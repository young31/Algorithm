# young 130ms, 248
T = int(input())
 
for i in range(1,T+1) :
    n = int(input())
    t =[]
    for j in (2,3,5,7,11) :
        k = 0
        while n % j == 0 :
            n /= j
            k += 1
        t.append(str(k))
    re = ' '.join(t)
    print('#%d'%i, re)