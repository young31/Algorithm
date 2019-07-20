# young 151ms, 411
for i in range(1, 11):
    t = int(input())
    mat = []
    n = 0
    for j in range(8):
        mat.append(list(input()))
    mat2 = list(zip(*mat))
    for j in range(8):
        for k in range(9-t):
            if list(mat[j][k:k+t]) == list(reversed(mat[j][k:k+t])):
                n += 1
            if list(mat2[j][k:k+t]) == list(reversed(mat2[j][k:k+t])):
                n += 1
    print('#%d'%i, n)