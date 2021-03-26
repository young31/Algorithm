# input
m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

n2 = 6
m2 = 6
board2 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

# answer: 

# algo
from copy import deepcopy

moves = [
    (1, 1), (1, 0), (0, 1), (0, 0)
] 

def serach(i, j, board):
    cur = board[i][j]
    if cur != 0 and (board[i+1][j+1] == board[i+1][j] == board[i][j+1] == cur):
        return True
    return False

def search_all(m, n, board):
    res = deepcopy(board)
    cnt = 0

    for i in range(m-1):
        for j in range(n-1):
            if serach(i, j, board):
                for di, dj in moves:
                    if res[i+di][j+dj] != 0:
                        cnt += 1
                    res[i+di][j+dj] = 0
    return res, cnt

def down(m, n, board):
    res = deepcopy(board)
    for i in range(1, m):
        for j in range(n):
            if res[i][j] == 0:
                for k in range(i, 0, -1):
                    res[k][j] = res[k-1][j]
                res[0][j] = 0

    return res

def solution(m, n, board):
    board = list(map(list, board))
    answer = 0

    while 1:
        board, cnt = search_all(m, n, board)
        if cnt == 0:
            break
        answer += cnt
        board = down(m, n, board)

    return answer

print(solution(m, n, board))
print(solution(m2, n2, board2))