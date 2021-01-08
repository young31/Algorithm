# young 115ms, 127
for i in range(1, int(input())+1):
    t = input()
    k = 1
    while t[0:k] != t[k:2*k]:
        k += 1
    print('#%d'%i, k)