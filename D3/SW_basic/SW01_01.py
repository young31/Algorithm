# young 169ms, 225
for i in range(1, 11):
    t = int(input())
    s = list(map(int, input().split( )))
    n = 0
    for j in range(2, t - 2):
        n += max(0, s[j] - max(s[(j - 2)],s[(j - 1)], s[(j + 1)], s[(j + 2)]))
    print('#%d'%i, n)