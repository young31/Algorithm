# input
n1 = 5
arr1 = [
    [0, 1, 0, 0, 2],
    [2, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 2, 0, 0]
]

n2 = 4
arr2 = [
    [1, 1, 1, 2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [2, 2, 2, 0]
]
# answer: yes

# algo
def search(arr, x, y, move):
    n = len(arr)
    res = []
    is_T = False

    if move == 0:
        dx, dy = 1, 0
    elif move == 1:
        dx, dy = -1, 0
    elif move == 2:
        dx, dy = 0, 1
    elif move == 3:
        dx, dy = 0, -1
    tmp = []
    while 1:
        nx = x+dx
        ny = y+dy
        if not is_feasible(n, nx, ny):
            break
        else:
            if arr[nx][ny] == 0:
                tmp.append((nx, ny))
            elif arr[nx][ny] == 2:
                is_T = True
                break
        x, y = nx, ny

    if is_T:
        if tmp:
            res += tmp
        else: # 선생이 있는데 막을 방법이 없으면 긴급상황(무조건 못 피함)
            return 'FLAG'

    return res

def is_feasible(n, x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def main(n, arr):
    students = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                students.append((i, j))
    
    # 막을 구간을 생성해서 해당 구간을 모두 방어하면 회피 성공으로 해결
    to_block = []
    for i, j in students:
        for m in range(4):
            tmp = search(arr, i, j, m)
            if tmp == 'FLAG':
                return 'NO'
            if tmp:
                to_block.append(tmp)
    
    # 막을 곳이 남아 있는지 체크
    remains = [True for _ in range(len(to_block))]
    n_block = 0
    for ib, block in enumerate(to_block):
        if not block:
            continue
        hist_remove = []
        # 해당 구간은 일단 막고 시작; 구간 내 몇개나 설치할 지는 아래에서 결정
        if remains[ib]:
            remains[ib] = False

            for i, xy in enumerate(block):
                remove = False
                for ib_, block_ in enumerate(to_block[ib+1:], ib+1):
                    # 공통 좌표가 있으면 해당 부분은 무조건 막고 진행; 해결된 구간도 함께 해결한 것으로 처리
                    if xy in block_:
                        remains[ib_] = False
                        remove = True
                        block_.remove(xy)
                        if n_block > 3:
                            return 'NO'

                if remove:
                    n_block += 1

                hist_remove.append(remove)
        # 공통된 부분이 없다면 해당 구간만 해결
        if sum(hist_remove) == 0:
            n_block += 1

    if n_block <= 3 and sum(remains) == 0:
        return 'YES'
    else:
        return 'NO'


print(main(n1, arr1))
print(main(n2, arr2))