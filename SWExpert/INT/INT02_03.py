# young 
for i in range(1, int(input())+1):
    t = list(map(int, input().split()))
    ab = [0, 0]
    for j in range(1, 3):
        start = 1
        end = t[0]
        k = int((start + end) / 2)
        while k != t[j]:
            if k < t[j]:
                start = k
            elif k > t[j]:
                 end = k
            k = int((start + end) / 2)
            ab[(j-1)] += 1
    print('#%d'%i, end = ' ')
    if ab[0] == ab[1]:
        print(0)
    elif ab[0] > ab[1]:
        print('B')
    else : print('A')