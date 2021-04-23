board = [[0,0,1,1],[1,1,1,1]]
board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

# 반복문 효율성 통과 못함 => DP
def solution(board):
    c = len(board[0])
    r = len(board)
    answer = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 1:
                m = min(r-i, c-j)
                for k in range(int(answer**0.5), m+1):
                    # s = sum([sum(board[i][j:j+k]) for i in range(i, i+k)])
                    s = all([all(board[i][j:j+k]) for i in range(i, i+k)])
                    print(s)
                    print(i, j, k, s, m)
                    if s and answer < k**2:
                        answer = k**2
                    # else:
                    #     break
                    
    print(answer)
    return answer

def solution(board):
    c = len(board[0])
    r = len(board)
    dp = [[0]*(c+1)]
    for b in board:
        dp.append([0]+b)
    dp.append([0]*(c+1))
    answer = 0
    for i in range(1, r+1):
        for j in range(1, c+1):
            if i==1 and j==1:
                continue
            elif dp[i][j] != 0:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1

    answer = max(map(lambda x: max(x), dp))**2
    return answer

solution(board)
