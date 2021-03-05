# input
n = 5
arr = [
    [7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]
]

# answer: 30

# algo
def flatten(arr):
    res = []
    for i in range(len(arr)):
        res += arr[i].copy()
    return res

def solution(n, arr):
    arr = flatten(arr)

    for i in range(1, n):
        idx = int(i*(i+1)/2)
        min_ = int(((i-1)*i)/2)
        max_ = idx-1
        for j in range(i+1):
            arr[idx+j] += max(
                arr[max(idx-i+j-1, min_)], arr[min(idx-i+j, max_)]
            )
    print(max(arr))

solution(n, arr)