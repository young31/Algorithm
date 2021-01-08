# young 124ms, 166
n = int(input())
a=[]
for i in range(1,n+1) :
    j = str(i)
    t = j.count('3') + j.count('6') + j.count('9')
    if t >0 :
        j = '-'*t
    print(j, end=' ')