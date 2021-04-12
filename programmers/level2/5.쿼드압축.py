arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

c = [0, 0]

def check(arr):
    n = len(arr)
    init = arr[0][0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != init:
                return False
    return True

def split(arr):
    n = len(arr)
    mid = n // 2

    arrs = [[] for _ in range(4)]
    for i in range(n):
        if i < mid:
            arrs[0].append(arr[i][:mid])
            arrs[1].append(arr[i][mid:])
        else:
            arrs[2].append(arr[i][:mid])
            arrs[3].append(arr[i][mid:])

    return arrs

def search(arr):
    global c
    if len(arr) == 1:
        c[arr[0][0]] += 1
        return 
    elif check(arr):
        c[arr[0][0]] += 1
        return 

    else:
        n = len(arr)
        mid = n//2
        for a in split(arr):
            search(a)

def solution(arr):
    global c
    search(arr)
    print(c)
    return c

solution(arr)