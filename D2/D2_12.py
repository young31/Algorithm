# young 126ms, 300
for i in range(1, int(input())+1):
    print('#%d'%i)
    n = int(input())
    t = []
    for j in range(n):
        t.append(list(input().split( )))
    col = list(map(list, zip(*t)))
    for j in range(n):
        print(''.join(reversed(col[j])), ''.join(reversed(t[-(j+1)])), ''.join(col[-(j+1)]))