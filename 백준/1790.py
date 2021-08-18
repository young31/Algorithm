import math

def num_to_n(n):
    k = 10
    c = 1
    ans = 0
    while 1:
        if n < k:
            ans += (n - k//10+1)*c
            return ans
        else:
            if c == 1:
                ans += 9
            else:
                ans += (k - k//10)*c
        c += 1
        k = 10**c

def num_in_k(n):
    k = 10
    c = 1
    ans = n
    while 1:
        if ans < (k - k//10)*c:
            num = math.ceil(ans / c)-1 + k//10
            if ans == 0:
                idx = 0
            else:
                idx = ans%c
                if idx == 0:
                    idx = c
                idx -= 1
            return str(num)[idx]
        else:
            if c == 1:
                ans -= 9
            else:
                ans -= (k - k//10)*c
        c += 1
        k = 10**c

n, k = map(int, input().split())
len_n = num_to_n(n)
if len_n < k:
    print(-1)
else:
    print(num_in_k(k))
