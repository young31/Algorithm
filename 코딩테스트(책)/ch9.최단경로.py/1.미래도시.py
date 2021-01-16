# input
n1, m1 = 5, 7
x1, k1 = 4, 5
input1 = {
    1: {2: 1, 3: 1, 4: 1},
    2: {4: 1},
    3: {4: 1, 5: 1},
    4: {5: 1}
}

n2, m2 = 4, 2
x2, k2 = 3, 4
input2 = {
    1: {3: 1},
    2: {4: 1},
}
# answer: 3, -1

# algo
inf = int(1e10)
def preprocess(inputs, n):
    arr = [[inf for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        arr[i][i] = 0
    for k1, dct in inputs.items():
        for k2, v in dct.items():
            arr[k1][k2] = v
            arr[k2][k1] = v

    return arr

def find(start, middle, end, arr):
    n = len(arr)
    ar = arr.copy()
    for i in [start, middle]:
        for j in [middle, end]:
            for k in range(1, n):
                ar[i][j] = min(ar[i][j], ar[i][k]+ar[k][j])

    a = (ar[start][middle])
    b = (ar[middle][end])
    if a == inf or b == inf:
        print(-1)
    else:
        print(a+b)

arr1 = preprocess(input1, n1)
find(1, k1, x1, arr1)

arr2 = preprocess(input2, n2)
find(1, k2, x2, arr2)