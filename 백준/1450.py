from bisect import bisect_right

n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = len(arr)//2

a1_ = arr[:m]
a2_ = arr[m:]

a1 = [0]
a2 = [0]

for a in a1_:
    tmp = [x+a for x in a1]
    a1 += tmp

for a in a2_:
    tmp = [x+a for x in a2]
    a2 += tmp

a2.sort()

ans = 0
for a in a1:
    ans += bisect_right(a2, k-a)
    
print(ans)
