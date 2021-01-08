# young 
for i in range(1, int(input())+1):
    n = int(input())
    t = list(map(int, input().split( )))
    t = sorted(t)
    index = []
    for j in range(int(n/2)):
        index.append(-(j+1))
        index.append(j)
    print('#%d'%i, end=' ')
    for k in index[:10]:
        if k == index[9]:
            print(t[k])
        else: print(t[k], end =' ')
                     
               