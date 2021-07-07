n, k = map(int, input().split())

if k == 1:
    print(1)
else:
    arr = [1 for _ in range(n+1)]
    cnt = 1

    while cnt != k:
        tmp = [sum(arr[:i+1]) for i in range(n+1)]
        cnt += 1
        arr = tmp

        # print(tmp)
    print(tmp[-1]%1000000000)

