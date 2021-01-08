# young 163ms, 412
T = int(input())
for i in range(1, T+1) :
    [a, b] = list(map(int,input().split( )))
    l = {}
    for j in range(1,a+1) :
        l[j] = list(map(int, input().split( )))
    p = []
    for k in range(0, a-b+1) :
        for o in range(0, a-b+1) :
            v=0
            for m in range(0,b) :
                v += sum(l[k+m+1][o:o+b])
            p.append(v)
    print("#%d"%i,end=' ')
    print(max(p))