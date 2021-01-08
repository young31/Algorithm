# input
n, m = 4, 4
init = (1, 1, 0)
mp = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
# answer: 3

# algo
dir_map = {
    0: (-1, 0),
    1: (0, -1),
    2: (1, 0),
    3: (0, 1)
}

def is_feasible(state, head):
    y, x = dir_map[head]
    if mp[state[0]+y][state[1]+x] == 0:
        return True
    return False

def step(state, head, cnt):
    global mp
    for h in range(head, head+4): # 새로운 곳을 발견하면 가고 cnt + 1
        h %= 4
        if is_feasible(state, h):
            y = dir_map[h][0]
            x =  dir_map[h][1]
            state_next = [
                state[0] + y, state[1] + x
            ]

            mp[state[0] + y][state[1] + x] = 2
            done = False
            cnt += 1
            return state_next, h, done, cnt
    
    # 새로운 곳이 없는 경우 뒤로 갈 수 있으면 가고 아니면 종료
    done = is_done(state, head)
    if done:
        return state, head, True, cnt
    else:
        y, x = dir_map[head]
        state_next = [
            state[0] + y*-1, state[1] + x*-1
        ]
        return state_next, head, False, cnt

def is_done(state, head):
    y, x = dir_map[head]
    if mp[state[0] + y*-1][state[1] + x*-1] == 1:
        return True
    return False

def main():
    state = [init[0], init[1]]
    head = init[2]
    done = False
    cnt = 0
    while not done:
        state, head, done, cnt = step(state, head, cnt)
        # for i in range(4): print(mp[i])
        # print(state, head, done)
        # print()
    print(cnt)

main()


