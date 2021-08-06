import sys
sys.setrecursionlimit(10 ** 9)

a, b, c = map(int, input().split())

answer = 0
visited = [[0 for _ in range(1501)] for _ in range(1501)]
s = a + b + c


def dfs(a, b):
    global s, answer
    if visited[a][b]:
        return
    visited[a][b] = 1
    c = s - a - b
    if a == b == c:
        answer = 1
        return

    temp = [a, b, c]
    for i in range(3):
        for j in range(3):
            if temp[i] > temp[j]:
                dfs(temp[i] - temp[j], temp[j] * 2)


if s % 3 != 0:
    print(0)
else:
    dfs(a, b)
    print(answer)