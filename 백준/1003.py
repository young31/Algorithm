N = int(input())
memo = {0: [1, 0], 1: [0, 1]}
for _ in range(N):
    n = int(input())
    if n in memo.keys():
        print(*memo[n])
    else:
        for i in range(2, n+1):
            memo[i] = [
                memo[i-1][0]+memo[i-2][0], memo[i-1][1]+memo[i-2][1]
            ]

        print(*memo[n])
