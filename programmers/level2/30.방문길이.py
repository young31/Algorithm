dirs = "ULURRDLLU"
dirs = "LULLLLLLU"

# 길을 기준으로 해야하기 때문에 전후 좌표를 기준으로 pair 검토
def solution(dirs):
    answer = 0

    controller = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    board = [[False]*11 for _ in range(11)]
    state = (5, 5)
    board[5][5] = True
    pairs = []

    for d in dirs:
        i, j = state
        di, dj = controller[d]
        ni = i+di
        nj = j+dj
        if ni<0: ni = 0
        elif ni>10: ni = 10
        if nj<0: nj = 0
        elif nj>10: nj = 10

        if state+(ni, nj) not in pairs and state != (ni, nj):
            pairs.append(state+(ni, nj)) 
            pairs.append((ni, nj)+state)
            answer += 1

        state = (ni, nj)
    print(answer)

    return answer

solution(dirs)