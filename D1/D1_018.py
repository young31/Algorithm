# young 125ms, 128
T = input()
 
for i in range(1,4) :
    l = list(map(int, input().split()))
    t = sum(l)/10
    print("#%d %d" % (i, round(t)))