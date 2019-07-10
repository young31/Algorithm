# young
for i in range(1, int(input())+1):
    n, m = map(int, input().split( ))
    sam = []
    tsam= []
    s = 0
    print('#%d'%i, end =' ')
    for j in range(n):
        sam.append(list(input()))
    for j in range(n):
        em = []
        for k in range(n):
            em.append(sam[k][j])
        tsam.append(em)
    for j in range(n):
        for k in range(n-m+1):
            if sam[j][k:k+m+1] == list(reversed(sam[j][k:k+m+1])):
                print(''.join(sam[j][k:k+m+1]))
    for j in range(n):
        for k in range(n-m+1):
            if tsam[j][k:k+m+1] == list(reversed(tsam[j][k:k+m+1])):
                print(''.join(tsam[j][k:k+m+1]))