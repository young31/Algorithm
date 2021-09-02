from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    ops = input().strip()
    n = int(input())
    arr = deque(eval(input()))

    direction = 0
    error = False
    for op in ops:
        if op == 'R':
            direction = 1 - direction
        else:
            if not arr:
                error = True
                break
            else:
                if direction == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if error:
        print('error')
    else:
        if direction == 1:
            print('['+','.join(list(map(str, arr))[::-1])+']')
        else:
            print(str(list(arr)).replace(' ', ''))
