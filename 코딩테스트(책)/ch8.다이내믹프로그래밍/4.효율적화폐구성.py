# input
n1, m1 = 2, 15
arr1 = [2, 3]

n2, m2 = [3, 4]
arr2 = [3, 5, 7]
# answer: 5, -1

# algo
def main(n, arr):
    dp = [float('inf') for _ in range(n+1)]
    for i in range(n+1):
        if i in arr:
            # print('k')
            dp[i] = 1
        else:
            for a in arr:
                if i-a >= 0:
                    dp[i] = min(dp[i], dp[i-a]+1)

    if dp[-1] == float('inf'):
        print(-1)
    else:
        print(dp[-1])

main(m1, arr1)
main(m2, arr2)

