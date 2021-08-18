n = int(input())
arr = input().split()

def convert(arr):
    ans = 0
    for i, a in enumerate(arr[::-1]):
        ans += a*(10**i)
    return ans

def pad(num):
    if len(str(num)) < n+1:
        return '0'+str(num)
    return num

def search(ans, k):
    global used, min_, max_
    if k == n:
        a = convert(ans)
        if min_ > a:
            min_ = a
        if max_ < a:
            max_ = a
        return
    for num in nums:
        if not used[num]:
            if arr[k] == '<':
                if ans[-1] < num:
                    used[num] = True
                    search(ans+[num], k+1)
                    used[num] = False
            else:
                if ans[-1] > num:
                    used[num] = True
                    search(ans+[num], k+1)
                    used[num] = False

nums = list(range(10))
used = [False for _ in range(10)]
min_ = float('inf')
max_ = 0

for i in range(10):
    used[i] = True
    search([i], 0)
    used[i] = False

print(pad(max_))
print(pad(min_))