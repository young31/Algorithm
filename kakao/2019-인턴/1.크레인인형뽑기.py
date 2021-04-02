board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

from pprint import pprint
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
        pprint(board)
        idx, item = pick(board, m-1)
        if idx != -1:
            pack.insert(item)
            board[idx][m-1] = 0

    answer = pack.cnt
    return answer

print(solution(board, moves))