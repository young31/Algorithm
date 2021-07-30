n = int(input())
arr = []
for _ in range(n):
    arr += list(map(int, input().split()))
    
for i in range(1, n):
    idx = int(i*(i+1)/2)
    min_ = int(((i-1)*i)/2)
    max_ = idx-1
    for j in range(i+1):
        arr[idx+j] += max(
            arr[max(idx-i+j-1, min_)], arr[min(idx-i+j, max_)]
        )
print(max(arr))