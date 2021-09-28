board = [
    list(map(int, input().split())) for _ in range(9)
]

n = len(board)

def find_cand(i, j):
    total = set(range(1, 10))
    for k in range(9):
        total = total - set([board[i][k]])
        total = total - set([board[k][j]])
    s = i//3
    e = j//3
    for i in range(s*3, s*3+3):
        for j in range(e*3, e*3+3):
            total = total - set([board[i][j]])
    return list(total)

def is_feasible(i, j, v):
    for k in range(9):
        if board[i][k] == v or board[k][j] == v:
            return False

    s = i//3
    e = j//3
    for i in range(s*3, s*3+3):
        for j in range(e*3, e*3+3):
            if board[i][j] == v:
                return False
    return True


def match(x):
    global board
    if x == len(zeros):
        for b in board:
            print(*b)
        exit()
    i, j = zeros[x]
    # cand = find_cand(i, j)
    for v in cands[x]:
        if is_feasible(i, j, v):
            board[i][j] = v
            match(x+1)
            board[i][j] = 0

zeros = []
cands = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            zeros.append((i, j))
            cands.append(find_cand(i, j))

match(0)




# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0