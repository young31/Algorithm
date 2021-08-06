
def get_primes(n):
    a = [False,False] + [True]*(n-1)
    primes=[]
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

n = int(input())
if n == 1:
    print(0)
    exit()

primes = get_primes(n)
print(primes[-10:])
s = 0
e = 0
c = primes[0]
ans = 0
while s <= e < len(primes):
    if c == n:
        ans += 1

    if c >= n:
        c -= primes[s]
        s += 1
    elif e == len(primes)-1:
        break
    else:
        e += 1
        c += primes[e]

print(ans)