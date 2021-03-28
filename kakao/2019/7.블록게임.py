# input
board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
# answer: 2

# algo
availabel_form = [
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, -1), (2, 0)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, -2), (1, -1), (1, 0)],
    [(0, 0), (1, -1), (1, 0), (1, 1)]
]

def normalize(x):
    nx = sorted(x)
    mx, my = nx[0]
    nx = [(x-mx, y-my) for x, y in nx]
    return nx

def is_available(x):
    nx = normalize(x)

    if nx in availabel_form:
        return True
    return False

def is_feasible(i, j, n):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False

def check_upper(xy, board, target):
    x, y = xy
    n = len(board)

    if (is_feasible(x-1, y, n) and board[x-1][y] == target) or (is_feasible(x+1, y, n) and board[x+1][y] == target):
        return True

    else:
        while 1:
            if board[x][y] == target or board[x][y] == 0:
                x -= 1
                if x < 0:
                    return True
            else:
                return False

def solution(board):
    forms = {}
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                k = board[i][j]
                if k not in forms.keys():
                    forms[k] = [[i, j]]
                else:
                    forms[k].append([i, j])
    canidates = {}
    for k in forms.keys():
        if is_available(forms[k]):
            canidates[k] = forms[k]
    
    cnt = 0
    do_op = False
    while 1:
        do_op = False
        removed = []
        for k in canidates.keys():
            upper = [check_upper(c, board, k) for c in canidates[k]]
            if sum(upper) == 4:
                cnt += 1
                for i, j in canidates[k]:
                    board[i][j] = 0
                removed.append(k)
                do_op = True

        if not do_op:
            break
        else:
            for k in removed:
                canidates.pop(k)
    return cnt

print(solution(board))