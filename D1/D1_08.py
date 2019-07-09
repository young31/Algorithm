T = int(input())

for i in range(1,T+1) :
    N = list(map(int, input().split( )))
    a = N[0] // N[1]
    b = N[0] % N[1]
    print("#{} {} {}".format(i, a, b))
