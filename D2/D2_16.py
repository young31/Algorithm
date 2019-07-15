# young 138ms, 270
T = int(input())
 
for i in range(1,T+1) :
    [a1,b1,a2,b2] = list(map(int,input().split( )))
    a3 = a1 + a2
    if a3 >= 12 :
        a3 -= 12
    b3 = b1 + b2
    if b3 >= 60 :
        b3 -= 60
        a3 += 1
    c = [str(a3),str(b3)]
    print('#%d'%i,' '.join(c))