def encode(nums):
    m = len(nums)
    x = y = 0
    for i, n in enumerate(nums):
        k = 2**(m-i-1)
        if n == 1:
            y += k
        elif n == 3:
            x += k
        elif n == 4:
            x += k 
            y += k
    return x, y

def decode(x, y, n):
    res = [0 for _ in range(n)]
    for i in range(n):
        k = 2 ** (n-i-1)
        if x >= k and y >= k:
            res[i] = 4
            x -= k
            y -= k
        else:
            if x >= k:
                res[i] = 3
                x -= k
            elif y >= k:
                res[i] = 1
                y -= k
            else:
                res[i] = 2
    return res


a, b = input().split()
n = int(a)
b = list(map(int, list(b)))
d1, d2 = map(int, input().split())
k = 2 ** n

x, y = encode(b)

x -= d2
y += d1

if (not (0 <= x < k)) or (not (0 <= y < k)):
    print(-1)
else:
    ans = decode(x, y, n)
    ans = ''.join(list(map(str, ans)))
    print(ans)
