# young
for i in range(1, int(input()) +1):
    le = list(input())
    j = 0
    while len(le) != 1+j:
        if le[j] == le[j+1] :
            le.pop(j)
            le.pop(j)
            if j != 0:
                j -= 1
        else: j += 1
    print('#%d'%i, len(le))