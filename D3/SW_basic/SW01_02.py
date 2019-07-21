# young 175ms, 207
for i in range(1, 11):
    t = int(input())
    s = list(map(int, input().split( )))
    for j in range(t):
        s[s.index(max(s))] -= 1
        s[s.index(min(s))] += 1
    print('#%d'%i, max(s) - min(s))