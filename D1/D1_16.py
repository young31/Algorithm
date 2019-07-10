# young 120ms, 117
T = input()
 
for i in range(1,4) :
    l = list(map(int, input().split()))
    k = max(l)
    print("#%d %d" % (i,k))