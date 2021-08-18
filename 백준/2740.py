# 슈트라센 알고리즘
def empty_mat(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

def pointwise_sum(a, b, mode='add'):
    n = len(a)
    mat = empty_mat(n, n)
    for i in range(n):
        for j in range(n):
            if mode == 'add':
                mat[i][j] = a[i][j] + b[i][j]
            elif mode == 'sub':
                mat[i][j] = a[i][j] - b[i][j]
    return mat

def strassen(a, b, n):
    mat = empty_mat(n, n)
    if n == 1:
        mat[0][0] = a[0][0] * b[0][0]
        return mat

    n_ = n//2
    a_ = split(a, n_)
    b_ = split(b, n_)
    # print(a_)
    # print(b_)

    c_ = [
        empty_mat(n_, n_) for _ in range(4)
    ]

    m1 = strassen(pointwise_sum(a_[0], a_[3]), pointwise_sum(b_[0], b_[3]), n_)
    m2 = strassen(pointwise_sum(a_[2], a_[3]), b_[0], n_)
    m3 = strassen(a_[0], pointwise_sum(b_[1], b_[3], mode='sub'), n_)
    m4 = strassen(a_[3], pointwise_sum(b_[2], b_[0], mode='sub'), n_)
    m5 = strassen(pointwise_sum(a_[0], a_[1]), b_[3], n_)
    m6 = strassen(pointwise_sum(a_[2], a_[0], mode='sub'), pointwise_sum(b_[0], b_[1]), n_)
    m7 = strassen(pointwise_sum(a_[1], a_[3], mode='sub'), pointwise_sum(b_[2], b_[3]), n_)

    # print(m1)

    c_[0] = pointwise_sum(
        pointwise_sum(
            pointwise_sum(m1, m4), m5, mode='sub'
        ), m7
    )
    c_[1] = pointwise_sum(m3, m5)
    c_[2] = pointwise_sum(m2, m4)
    c_[3] = pointwise_sum(
        pointwise_sum(
            pointwise_sum(m1, m2, mode='sub'), m3
        ), m6
    )

    for i in range(n_):
        for j in range(n_):
            mat[i][j] = c_[0][i][j]
            mat[i][j+n_] = c_[1][i][j]
            mat[i+n_][j] = c_[2][i][j]
            mat[i+n_][j+n_] = c_[3][i][j]
    return mat

def split(a, n):
    m = [
        empty_mat(n, n) for _ in range(4)
    ]

    for i in range(n):
        for j in range(n):
            m[0][i][j] = a[i][j]
            m[1][i][j] = a[i][j+n]
            m[2][i][j] = a[i+n][j]
            m[3][i][j] = a[i+n][j+n]
    return m


n1, m1 = map(int, input().split())
mat1 = [
    list(map(int, input().split())) for _ in range(n1)
]

n2, m2 = map(int, input().split())
mat2 = [
    list(map(int, input().split())) for _ in range(n2)
]

N = max(n1, m1, m2)
s = 0
while N > 2**s:
    s += 1 
s = 2**s

for i in range(s):
    if i < n1:
        for j in range(s-m1):
            mat1[i].append(0)
    else:
        mat1.append([0]*s)

for i in range(s):
    if i < n2:
        for j in range(s-m2):
            mat2[i].append(0)
    else:
        mat2.append([0]*s)

mat = strassen(mat1, mat2, s)
for i in range(n1):
    for j in range(m2):
        print(mat[i][j], end=' ')
    print()