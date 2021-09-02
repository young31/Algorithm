import sys
input = sys.stdin.readline

def is_same(board):
    c = board[0][0]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] != c:
                return False
    return True

def search(board):
    global answer
    color = board[0][0]
    
    if is_same(board):
        answer += str(color)
    else:
        answer += '('
        m = len(board)//2
        tmp1 = [board[i][:m] for i in range(m)]
        search(tmp1)
        tmp2 = [board[i][m:] for i in range(m)]
        search(tmp2)
        tmp3 = [board[m+i][:m] for i in range(m)]
        search(tmp3)
        tmp4 = [board[i+m][m:] for i in range(m)]
        search(tmp4)
        answer += ')'

n = int(input())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
answer = ''

search(arr)

print(answer)