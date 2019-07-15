# young 135ms, 532
T = int(input())
 
for i in range(1,T+1) :
    t={}
    for j in range(0,9) :
        t[j] = list(''.join(list(map(str,input().split( )))))
    t2 = list(zip(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8]))
    t3 = {}
    for k in range(0,3) :
        for l in range(0,3):
            t3[3*k+l] = list(t[3*k][3*l:3*l+3]+t[3*k+1][3*l:3*l+3]+t[3*k+2][3*l:3*l+3])
    n = 0
    for k in range(0,9) :
        n += len(set(t[k])) + len(set(t2[k])) + len(set(t3[k]))
    if n ==243 :
        print("#%d" %i, 1)
    else : print("#%d" %i, 0)