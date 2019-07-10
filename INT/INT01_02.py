# young 
for i in range(1, int(input()) + 1):
    a, b = tuple(map(int, input().split())), list(map(int, input().split()))
    b.append(a[1])
    n = 0
    j = 0
    t = a[0]
    while j < a[1]:
        if t == 0 :
            n = 1
            break
        if (j + t) in b:
            n += 1
            j += t
            t = a[0]
        else:
            t -= 1
    print('#%d'%i, n-1)