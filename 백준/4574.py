import sys
input = sys.stdin.readline

from pprint import pprint
print(ord('A'))
while 1:
    n = int(input())
    if n == 0:
        break

    board = [
        [0 for _ in range(9)] for _ in range(9)
    ]

    # dominos
    for _ in range(n):
        u, lu, v, lv = input().split()

        board[ord(lu[0])-65][int(lu[1])-1] = int(u)
        board[ord(lv[0])-65][int(lv[1])-1] = int(v)

    # numbers
    numbers = input().split()
    for i, num in enumerate(numbers, 1):
        board[ord(num[0])-65][int(num[1])-1] = i
    
    pprint(board)
