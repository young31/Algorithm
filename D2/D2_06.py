# young 132ms, 419
T = int(input())
 
for i in range(1, T+1) :
    t=int(input())
    n1=0
    n2=0
    for j in range(0,t) :
        k = list(map(int,input().split( )))
        if k[0] == 0 :
            n1 += n2
        elif k[0] == 1 :
            n2 += k[1]
            n1 += n2
        else :
            if n2 < k[1] :
                n2 = 0
                continue
            n2 -= k[1]
            n1 += n2
    print('#%d'%i, n1)