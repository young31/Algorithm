# input
n, m = 5, 6
maze = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
# answer: 10

# algo
avaliable_move = [
    (0, 1), (0, -1), (-1, 0), (1, 0)
]

def is_feasible(maze, cur, step):
    i, j = cur
    di, dj = step
    if 0 < i+di < n and 0 <= j+dj < m and maze[i+di][j+dj] == 1:
        return True
    return False

def main():
    from copy import deepcopy
    from pprint import pprint
    from collections import deque
    global maze
    # maze = [[0 for _ in range(m)]] + maze
    pprint(maze)
    init = (0, 0, 1)
    visited = deepcopy(maze)
    to_visit = deque()
    to_visit.append(init)
    n_step = 0
    while 1:
        n_step += 1
        cur = to_visit.popleft()
        for move in avaliable_move:
            if is_feasible(maze, cur[:-1], move):
                next_loc = (cur[0]+move[0], cur[1]+move[1])
                ni, nj = next_loc
                if visited[ni][nj] != 2:
                    if next_loc == (n-1, m-1):
                        print(n_step)
                        return cur[2]+1
                    to_visit.append((cur[0]+move[0], cur[1]+move[1], cur[2]+1))
                    visited[ni][nj] = 2

print(main())
        
