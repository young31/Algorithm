n = int(input())

i = 1
ans = 0
while 1:
    if n < 10**i:
        if i == 1:
            ans += i*(n-(10**(i-1)))
        else:
            ans += i*((n-(10**(i-1)))+1)
        break
    else:
        k = 10**i - 10**(i-1)
        ans += i*k
    i += 1

print(ans)