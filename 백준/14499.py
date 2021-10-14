
def roll(d, state):
    if d == 4:
        nxt_state = [
            state[2], state[1], state[5], state[3], state[0], state[4]
        ]
    elif d == 1:
        nxt_state = [
            state[1], state[5], state[2], state[0], state[4], state[3]
        ]
    elif d == 2:
        nxt_state = [
            state[3], state[0], state[2], state[5], state[4], state[1]
        ]
    elif d == 3:
        nxt_state = [
            state[4], state[1], state[0], state[3], state[5], state[2]
        ]
    return nxt_state

def is_feasible(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False
    
state = [1, 2, 3, 4, 5, 6]
values = {i: 0 for i in range(1, 7)}

n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

rules = list(map(int, input().split()))
for r in rules:
    # print(arr)
    if r == 1:
        y += 1
        if is_feasible(x, y):
            state = roll(r, state)
            if arr[x][y] == 0:
                arr[x][y] = values[state[-1]]
            else:
                values[state[-1]] = arr[x][y]
                arr[x][y] = 0
            print(values[state[0]])
        else:   
            y -= 1
            continue
    if r == 2:
        y -= 1
        if is_feasible(x, y):
            state = roll(r, state)
            if arr[x][y] == 0:
                arr[x][y] = values[state[-1]]
            else:
                values[state[-1]] = arr[x][y]
                arr[x][y] = 0
            print(values[state[0]])
        else:   
            y += 1
            continue
    if r == 3:
        x -= 1
        if is_feasible(x, y):
            state = roll(r, state)
            if arr[x][y] == 0:
                arr[x][y] = values[state[-1]]
            else:
                values[state[-1]] = arr[x][y]
                arr[x][y] = 0
            print(values[state[0]])
        else:   
            x += 1
            continue
    if r == 4:
        x += 1
        if is_feasible(x, y):
            state = roll(r, state)
            if arr[x][y] == 0:
                arr[x][y] = values[state[-1]]
            else:
                values[state[-1]] = arr[x][y]
                arr[x][y] = 0
            print(values[state[0]])
        else:   
            x -= 1
            continue
