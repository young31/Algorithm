# young 119ms, 329
T = int(input())
 
for i in range(1,T+1) :
    l = list(input())
    y = int("".join(l[0:4])) ; m = float("".join(l[4:6])) ; d = float("".join(l[6:8]))
    if d < 1 or m < 1 or (m == 2 and d > 28) or (m == 4 | 6 | 9 | 11 and d > 30) :
        print("#%d -1" % i)
    else :
        print("#%d %04.0f/%02.0f/%02.0f" % (i, y, m, d))