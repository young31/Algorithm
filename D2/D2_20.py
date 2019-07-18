# young 123ms, 153
for i in range(1, int(input())+1):
    t = int(input())
    if t % 2 == 1:
        print('#%d'%i, int(t/2)+1)
    else:
        print('#%d'%i, int(-t/2))