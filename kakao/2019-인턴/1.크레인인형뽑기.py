board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]

# solution 1
from collections import deque

def get(board, move):
    n = len(board)
    pick = 0
    for i in range(n):
        if board[i][move-1] != 0:
            pick = board[i][move-1]
            board[i][move-1] = 0
            break
    return pick
        

def solution(board, moves):
    bucket = deque()
    answer = 0
    for move in moves:
        pick = get(board, move)
        if pick != 0:
            if len(bucket) < 1:
                bucket.append(pick)
            else:
                if bucket[-1] == pick:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(pick)

    return answer

# solution 2
from collections import deque

def pick(board, col):
    n = len(board)
    for i in range(n):
        if board[i][col] != 0:
            return i, board[i][col]

    return -1, -1

class Pack:
    def __init__(self):
        self.items = deque([])
        self.cnt = 0

    def insert(self, item):
        if not self.items:
            self.items.append(item)
        elif self.items[-1] == item:
                self.items.pop()
                self.cnt += 2
        else:
            self.items.append(item)


def solution(board, moves):
    answer = 0
    pack = Pack()
    for m in moves:
        idx, item = pick(board, m-1)
        if idx != -1:
            pack.insert(item)
            board[idx][m-1] = 0

    answer = pack.cnt
    return answer