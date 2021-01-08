# young 131ms, 267
T = int(input())
 
for i in range(1,T+1) :
    t = int(input())
    n =[]
    for j in range(0,t) :
        a = input().split( )
        n.append(a[0]*int(a[1]))
    n = ''.join(n)
    print('#%d'%i)
    for k in range(0,len(n)//10 +1) :
        print(n[10*k:10*k+10])