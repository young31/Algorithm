n = int(input())

if n == 1:
    print(3)
else:
    arr = [1, 1, 1]
    for _ in range(1, n):
        a = sum(arr)
        b = arr[0] + arr[1]
        c = arr[0] + arr[2]
        arr = [a, b, c]
    print(sum(arr)%9901)