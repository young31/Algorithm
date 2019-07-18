# young 176ms, 761
T = int(input())
def score_(a,b) :
    b.sort()
    c = len(b) - b.index(a)
    n = len(b)/10
    if c <= n :
        return 'A+'
    elif c <= n*2 :
        return 'A0'
    elif c <= n*3 :
        return 'A-'
    elif c <= n*4 :
        return 'B+'
    elif c <= n*5 :
        return 'B0'
    elif c <= n*6 :
        return 'B-'
    elif c <= n*7 :
        return 'C+'
    elif c <= n*8 :
        return 'C0'
    elif c <= n*9 :
        return 'C-'
    else : 
        return 'D+'
     
for i in range(1,T+1) :
    [a,b] = list(map(int, input().split( )))
    s =[]
    for j in range(1,a+1) :
        [s1,s2,s3] = list(map(int, input().split( ))) 
        s.append((4*s1+4*s2+2*s3))
        if j == b :
            tar = s[-1]
    print('#%d'%i,score_(tar,s))