n = int(input())
arr = list(map(int, input().split()))
k = int(input())

arr.sort()
cnt = 0

s = 0
e = n-1 # 뒤에서 부터 훑으며 와야 함; 앞에서 같이 가는 것으로 생각해서 한참 허덕임
while s != e:
    m = arr[s] + arr[e]
    if m == k:
        cnt += 1
        e -= 1
    elif m < k:
        s += 1
    else:
        e -= 1
        
print(cnt)