n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

k = int(input())
change = []
for _ in range(k):
    a, b = input().split()
    change.append((int(a), b))

cur = (0, 0)
body = [cur]
head = 1
c = 0
while 1:
    c += 1
    i, j = body[-1]
    if head == 0:
        i -= 1
    elif head == 1:
        j += 1
    elif head == 2:
        i += 1
    elif head == 3:
        j -= 1

    if i < 0 or i >= n or j < 0 or j >= n: # 벽
        break
    elif arr[i][j] == 2: # 자신
        break

    else:
        body.append((i, j))
        if arr[i][j] == 1:
            arr[i][j] = 2
        else:
            arr[i][j] = 2
            ti, tj = body.pop(0)
            arr[ti][tj] = 0

    if change and c == change[0][0]:
        if change[0][1] == 'L':
            head = (head - 1) % 4
        else:
            head = (head + 1) % 4

        change.pop(0)
print(c)


