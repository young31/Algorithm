def convert(x):
    if x == 0:
        return '0'
    elif x > 0:
        return '+'
    else:
        return '-'

def check(p, ans, n):
    for i in range(n):
        j = n-1
        c = convert(sum(p[i:j+1]))
        if c == ans[i][j]:
            continue
        else:
            return False
            
    return True

n = int(input())
target = input()

ans = []
idx = 0
for i in range(n, 0, -1):
    ans.append(' '*(n-i)+target[idx:idx+i])
    idx+=i

point = [0]
for i in range(n-1):
    point.append(point[-1]+(n-i))

done = False

def search(res, c, n=n, target=target):
    global done
    if done:
        return

    if c == n:
        if check(res, ans, c):
            print(str(res)[1:-1].replace(',', ''))
            done = True

    else:
        if target[point[c]] == '+':
            for i in range(1, 11):
                if check(res+[i], ans, c+1):
                    search(res+[i], c+1)

        elif target[point[c]] == '-':
            for i in range(1, 11):
                if check(res+[-i], ans, c+1):
                    search(res+[-i], c+1)

        else:
            if check(res+[0], ans, c+1):
                search(res+[0], c+1)

search([], 0)