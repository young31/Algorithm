# young 122ms, 134
T = int(input())
 
for i in range(1,T+1) :
    a= list(map(int,input().split( )))
    print("#%d"%i,round((sum(a) -(max(a)+min(a)))/8))