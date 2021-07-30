a, b, c = map(int, input().split())

k = 1
while 1:
    arr = [k%15, k%28, k%19]
    if arr[0] == 0:
        arr[0] = 15
    if arr[1] == 0:
        arr[1] = 28
    if arr[2] == 0:
        arr[2] = 19
    if arr == [a, b, c]:
        print(k)
        break
    else:
        k += 1
