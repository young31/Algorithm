# young 217ms, 369
for i in range(1, 11):
    input()
    l1=[]
    for j in range(100):
        l1.append(list(map(int, input().split( ))))
    l2 = tuple(map(list, zip(*l1)))
    s = 0
    s1 = 0
    s2 = 0
    for j in range(100):
        s = max(s, sum(l1[j]), sum(l2[j]))
    for k in range(100):
        s1 += l1[k][k]
        s2 += l1[99-k][99-k]
    print('#%d'%i, max(s, s1, s2))