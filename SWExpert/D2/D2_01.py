# young 196ms, 226
T = int(input())
 
for i in range(1, T+1) :
    num = int(input())
    n = list(map(int, input().split( )))
    n2 = list(set(n))
    t = []
    for j in n2 :
        t.append(n.count(j))
    print('#%d'%i,n2[t.index(max(t))])