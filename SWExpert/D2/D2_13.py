# young 118ms, 192
T = int(input())
 
for i in range(1,T+1) :
    j = int(input())
    k = list(map(int, input().split( )))
    k.sort()
    k = list(map(str,k))
    k = ' '.join(k)
    print('#%d'%i, k)