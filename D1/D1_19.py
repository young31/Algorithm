# 116ms, 215, jeong

n = int(input())
for i in range(n):
    sum = 0
    num = list(map(int,input().split()))
    for j in range(10):
        if num[j] % 2 == 1:
            sum = sum + num[j]
    
    print('#{0} {1}'.format(i+1, sum))


# young 127ms, 176
T = input()
for i in range(1,4) :
    b = list(map(int, input().split( )))
    t=0
    for j in b :
        if j % 2 ==1 :
            t += j
    print("#{0} {1}".format(i, t))