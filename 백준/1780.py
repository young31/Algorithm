import sys
input = sys.stdin.readline

def check(arr):
    n = len(arr)
    s = arr[0][0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != s:
                return False
    return True

def search(arr):
    global dct
    n = len(arr)
    if check(arr):
        dct[arr[0][0]] += 1
    else:
        if n == 3:
            for i in range(3):
                for j in range(3):
                    dct[arr[i][j]] += 1
        else:
            k = n//3
            for i in range(0, n, k):
                for j in range(0, n, k):
                    tmp = [
                        arr[i+l][j:j+k] for l in range(k)
                    ]
                    search(tmp)

n = int(input())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

dct = {-1:0, 0: 0, 1: 0}

search(arr)

print(dct[-1])
print(dct[0])
print(dct[1])