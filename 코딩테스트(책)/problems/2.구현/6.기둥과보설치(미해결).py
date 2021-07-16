# input

# answer: 

# algo
from pprint import pprint
def is_feasible_bo(frame, x, y):
    if frame[x][y-1] in [1, 3] or (frame[x][y+1] == 2 and frame[x][y-1] == 2):
        return True
    return False

def is_feasible_gi(frame, x, y):
    if x == 0 or frame[x][y] == 2 or frame[x][y-1] == 1:
        return True
    return False

def is_in(n, xy):
    x, y = xy
    if 0 <= x <= n:
        return True
    return False

def do_op(frame, ops):
    n = len(frame)
    x, y, c, b = ops[:2] # x, y, class, build
    if b == 0: # 삭제
        if c == 0: # 기둥
            if frame[x][y+1] == 2:
                if (frame[x][y+1] == 2 and frame[x][y-1] == 2):
                    frame[x][y] -= 1
        else:
            pass
    else: # 설치
        if c == 0: # 기둥
            if is_feasible_gi(frame, x, y):
               frame[x][y] += 1
               frame[x][y+1] += 1

        else: # 보
            if is_feasible_bo(frame, x, y):
                frame[x][y] += 2
                frame[x+1][y] += 2

    return frame

    
