N = int(input())
for _ in range(N):
    n = int(input())
    arr = [
        list(map(int, input().split())) for _ in range(2)
    ]

    dp = [0, 0, 0] # x 상 하  뜯었을 경우

    for i in range(n):
        a = max(dp) # i 안뜯으면 이전에서 최대값
        b = arr[0][i] + max(dp[0], dp[2]) # 위에 뜯을려면 그 전에 안뜯거나 아래 뜯
        c = arr[1][i] + max(dp[0], dp[1]) # 아래 경우
        dp = [a, b, c]
    print(max(dp))