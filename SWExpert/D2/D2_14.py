# young 122ms, 242
T = int(input())
 
for i in range(1, T+1) :
    a = int(input())
    n = []
    for j in (50000,10000,5000,1000,500,100,50,10) :
        t = a // j
        n.append(str(t))
        a -= j*t
    re = ' '.join(n)
    print('#%d'%i)
    print(re)