# young 
for i in range(1, int(input()) + 1):
    T = int(input())
    n = list(input())
    np = sorted(list(set(n)),reverse=True)
    k = []
    for j in range(len(np)):
        k.append(n.count(np[j]))
    print('#%d' % i, np[k.index(max(k))], max(k))
    