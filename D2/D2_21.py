# young 120ms, 188
T = int(input())
for i in range(1, T+1) :
    l = list(input())
    a = "".join(l)
    l.reverse()
    b = "".join(l)
    if  a== b :
        print("#%d 1"%i)
    else : print("#%d 0" % i)