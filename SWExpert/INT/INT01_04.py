# young 
for i in range(1, int(input())+1):
    t = tuple(map(int, input().split( )))
    n = tuple(map(int, input().split( )))
    k = []
    for j in range(t[0]-t[1]+1):
        k.append(sum(n[j:j+t[1]]))
    print('#%d'%i, max(k)-min(k))
                                 