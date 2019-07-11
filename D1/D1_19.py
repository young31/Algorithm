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

# young 125ms, 140
for i in range(1, int(input()) + 1):
    n = list(filter(lambda x : x % 2 ==1, list(map(int, input().split( )))))
    print('#%d'%i, sum(n))
## 코드는 짧아지는데 실행속도는 못따라가네요ㅠ
