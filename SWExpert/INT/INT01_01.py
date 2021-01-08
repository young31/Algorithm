# young 
for i in range(1,int(input())+1) :
    n = int(input())
    t = set(map(int, input().split( )))
    print('#%d'%i, max(t) - min(t))