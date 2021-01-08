# input
n = 5
directions = ['R', 'R', 'R', 'U', 'D', 'D']
# answer: (3, 4)

# algo
dir_map = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

def is_feasible(n, cur, direction):
    y, x = dir_map[direction]
    if 0 < cur[0] + y <= n and 0 < cur[1] + x <= n:
        return True
    
    return False

def step(n, cur, direction):
    if is_feasible(n, cur, direction):
        y, x = dir_map[direction]
        return (cur[0]+y, cur[1]+x)
    else:
        return cur

def main():
    cur = (1, 1)
    for d in directions:
        cur = step(n, cur, d)
        # print(d, cur)
    print(cur)

main()




