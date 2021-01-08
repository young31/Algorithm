# young 130ms, 254
T = int(input())
def relu(a, b) :
    if a >= b :
        return 0
    else :
        return b-a
     
for i in range(1,T+1) :
    t = list(map(int,input().split( )))
    k = min(t[0]*t[4] , t[1] + relu(t[2],t[4])*t[3])
    print('#%d'%i, k)