n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))


arr.sort()
for k in arr2:
    done = False
    if arr[0] == k or arr[n-1] == k:
        print(1)
        continue
    s = 0
    e = n-1
    while s <= e < n:
        mid = (s+e)//2
        if arr[mid] == k:
            print(1)
            done = True
            break
        elif arr[mid] < k:
            s = mid+1
        else:
            e = mid-1
    
    if not done:
        print(0)