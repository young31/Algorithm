n = int(input())

if n == 1:
    print(1)
else:
    dp = {
        1: 1,
    }
    nears = [1]
    for i in range(2, n+1):
        if int(i**0.5) == i**0.5:
            dp[i] = 1
            nears.append(i)
        else:
            ks = [
                dp[nears[-j]] + dp[i-nears[-j]] for j in range(len(nears)//2+1)
            ]
            dp[i] = min(ks)

    # print(i, nears)
    print(dp[n])
