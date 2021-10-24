from collections import deque, defaultdict

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

def false(): return False

def get_shape(i1, j1, i2, j2):
    res = []
    for i in range(i1, i2+1):
        res.append((i, j1))
        res.append((i, j2))
    for j in range(j1, j2+1):
        res.append((i1, j))
        res.append((i2, j))
    
    return res

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    for i in range(len(rectangle)):
        rectangle[i] = list(map(lambda x: 2*x, rectangle[i]))
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    mi2 = max([rec[2] for rec in rectangle])
    mj2 = max([rec[3] for rec in rectangle])

    arr = [[2 for _ in range(mj2+1)] for _ in range(mi2+1)]

    for rec in rectangle:
        shape = get_shape(*rec)
        for i, j in shape:
            if arr[i][j] == 2:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i][j] * 1
        
        for i in range(rec[0]+1, rec[2]):
            for j in range(rec[1]+1, rec[3]):
                arr[i][j] = arr[i][j] * 0

    for a in arr[::-1]: print(a)
    print()

    visited = defaultdict(false)

    que = deque([])
    que.append((characterX, characterY, 0))
    visited[(characterX, characterY)] = True
    while que:
        x, y, c = que.popleft()
        for dx, dy in moves:
            nx = x+dx; ny = y+dy
            if nx == itemX and ny == itemY:
                return (c+1)//2

            if 0 <= nx <= mi2 and 0 <= ny <= mj2 and arr[nx][ny] == 1 and not visited[(nx, ny)]:
                que.append((nx, ny, c+1))
                visited[(nx, ny)] = True

    return answer

rectangle = [[2,2,5,5],[1,3,6,4],[3,1,4,6]]
characterX, characterY, itemX, itemY = 1, 4, 6, 3
print(solution(rectangle, characterX, characterY, itemX, itemY))