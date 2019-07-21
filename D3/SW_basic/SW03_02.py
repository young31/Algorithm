# young 16122ms, 498
def find(x, y):
    for t in range(100, 0, -1):
        for j in range(100):
            for k in range(101 - t):
                if list(x[j][k:k + t]) == list(reversed(x[j][k:k + t])):
                    return t
                if list(y[j][k:k + t]) == list(reversed(y[j][k:k + t])):
                    return t
 
 
for i in range(1, 11):
    t = int(input())
    mat = []
    for j in range(100):
        mat.append(list(input()))
    mat2 = list(zip(*mat))
    print('#%d'%i, find(mat, mat2))