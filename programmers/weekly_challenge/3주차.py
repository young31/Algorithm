from collections import deque

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

def find(df, target):
    # board -> target=0, table -> target=1
    n = len(df)
    visited = [[False for _ in range(n)] for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if df[i][j] == target and not visited[i][j]:
                tmp = []
                que = deque()
                visited[i][j] = True
                que.append((i, j))
                while que:
                    x, y = que.popleft()
                    tmp.append((x, y))
                    for dx, dy in moves:
                        nx = x+dx
                        ny = y+dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and df[nx][ny] == target:
                            que.append((nx, ny))
                            visited[nx][ny] = True
                if target == 0:
                    res.append((make_df(tmp), len(tmp)))
                else:
                    res.append(make_df(tmp))
    return res

def pad(cord):
    xs = [c[0] for c in cord]
    ys = [c[1] for c in cord]

    n = max(ys) - min(ys) + 1
    m = max(xs) - min(xs) + 1

    arr = [[0 for _ in range(n)] for _ in range(m)]

    for x, y in cord:
        arr[x][y] = 1

    return arr

def make_df(cord):
    n = min([c[0] for c in cord])
    m = min([c[1] for c in cord])

    cord = list(map(lambda x: (x[0]-n, x[1]-m), cord))
    return pad(cord)

def rotate_90(arr):
    n = len(arr)
    m = len(arr[0])

    res = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            res[j][n-i-1] = arr[i][j]

    return res

def is_match(a, b):
    na = len(a)
    nb = len(b)
    ma = len(a[0])
    mb = len(b[0])

    if na != nb or ma != mb:
        return False

    for i in range(na):
        for j in range(ma):
            if a[i][j] != b[i][j]:
                return False

    return True

def solution(game_board, table):
    answer = 0

    to_match = find(game_board, 0)
    cands = find(table, 1)

    for t, c in to_match:
        done = False
        tmp = t.copy()
        for _ in range(4):
            tmp = rotate_90(tmp)
            for j in range(len(cands)):
                if is_match(tmp, cands[j]):
                    answer += c 
                    done = True
                    cands.pop(j)
                    break
            if done:
                break

    return answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
solution(game_board, table)