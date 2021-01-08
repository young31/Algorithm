# young
for i in range(1, int(input())+1):
    s1 = list(set(input()))
    s2 = list(input())
    n = []
    for j in range(len(s1)):
        c = s2.count(s1[j])
        n.append(s2.count(s1[j]))
    print('#%d'%i, max(n))
    