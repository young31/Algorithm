moves1 = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

moves2 = [
    (2, 0), (-2, 0), (0, 2), (0, -2)
]

moves2_banned = [
    (1, 0), (-1, 0), (0, 1), (0, -1)
]

moves3 = [
    (1, 1), (-1, -1), (1, -1), (-1, 1)
]

def is_feasible(i, j):
    if 0 <= i < 5 and 0 <= j < 5:
        return True
    return False

def find(i, j, place):
    # 바로 붙어 있음
    for di, dj in moves1:
        ni = i+di
        nj = j+dj
        if is_feasible(ni, nj) and place[ni][nj]=='P':
            return 1
        
    for idx, (di, dj) in enumerate(moves2):
        ni = i+di
        nj = j+dj
        ni_ban = i+moves2_banned[idx][0]
        nj_ban = j+moves2_banned[idx][1]

        if is_feasible(ni, nj) and place[ni][nj] == 'P' and place[ni_ban][nj_ban] != 'X':
            return 1

    for di, dj in moves3:
        ni = i+di
        nj = j+dj
        if is_feasible(ni, nj) and place[ni][nj] == 'P' and (place[ni][j] !='X' or place[i][nj] != 'X'):
            return 1

    return 0

def solution(places):
    answer = []
    for place in places:
        done = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    t = find(i, j, place)
                    if t == 1:
                        print(i, j)
                        done = True
                        break
            if done:
                break

        if done:
            answer.append(0)
        else:
            answer.append(1)

    print(answer)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)