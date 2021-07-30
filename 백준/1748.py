n = int(input())

ans = 0
i = 1
while 1:
    if n < 10**i:
        ans += (n - 10**(i-1)+1) * i
        break
    else:
        ans += (10**i - 10**(i-1)) * i
        i += 1

print(ans)