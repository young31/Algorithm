n = int(input())

if n == 1:
    print(9)

else:
    slot = [0] + [1 for _ in range(9)]
    for _ in range(n-1):
        tmp = [0 for _ in range(10)]
        for i in range(10):
            if i-1>=0:
                tmp[i-1] += slot[i]
            if i+1<10:
                tmp[i+1] += slot[i]
        slot = tmp
    print(sum(slot)%1000000000)