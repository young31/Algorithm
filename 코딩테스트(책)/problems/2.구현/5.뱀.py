# input
n1 = 6; k1= 3; d1 = 3
apples1 = [(3, 4), (2, 5), (5, 3)]
rotation1 = [(3, 'D'), (15, 'L'), (17, 'D')]

n2 = 10; k2 = 4; d2 = 4
apples2 = [(1, 2), (1, 3), (1, 4), (1, 5)]
rotation2 = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]

n3 = 10; k3 = 5; d3 = 4
apples3 = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
rotation3 = [(8, 'D'), (10, 'D'), (11, 'D', (13, 'L'))]
# answer: 9, 21, 13

# algo
from copy import deepcopy
from pprint import pprint
HEADING = [
    (0, 1), (1, 0), (0, -1), (-1, 0)
]
class Snake:
    def __init__(self, map_):
        self.length = 1
        self.loc = [[0, 0]]
        self.moves = []
        self.map = map_
        self.n = len(map_)

    def move(self, d):
        self.moves.append(d)
        n = self.length
        f1, f2 = self.loc[-1]
        for i in range(n):
            l, r = HEADING[self.moves[-i-1]]
            self.loc[i][0] += l
            self.loc[i][1] += r

        # l, r = self.loc[0]
        self.loc.append([f1, f2])


def is_feasible(map_, loc):
    n = len(map_)
    for l, r in loc:
        if 0 > l or l >= n or 0 > r or r >= n:
            return False
    
        if loc.count([l, r]) > 1:
            return False
    return True

def main(n, apples, rotation):
    heading = 0
    map_ = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in apples:
        map_[i-1][j-1] = 1

    snake = Snake(map_)

    t = 1
    while 1:
        if rotation:
            if rotation[0][0]+1 == t: # t초 후 이므로 1을 더해줌
                rot = rotation[0][1]
                if rot == 'D':
                    heading = (heading+1)%4
                elif rot == 'L':
                    heading -=1 
                    if heading < 0:
                        heading = 5 - heading
                rotation.pop(0)
        
        snake.move(heading)

        if not is_feasible(map_, snake.loc):
            return t
        else:
            l, r = snake.loc[0]
            if snake.map[l][r] == 1:
                snake.length += 1
                snake.map[l][r] = 0
            else:
                snake.loc.pop()

        t += 1

        
print(main(n1, apples1, rotation1))
print(main(n2, apples2, rotation2))
print(main(n3, apples3, rotation3))
