from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
n = 8
arr = [10, 20, 30, 5, 10, 20, 30]

lis = [arr[0]]

for a in arr[1:]:
    if lis[-1] < a:
        lis.append(a)
    else:
        idx = bisect_left(lis, a)
        lis[idx] = a
print(len(lis))
    
