def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])

    def get_start(i, j):
        res = []
        if i == 0:
            res.append(0)
        if j == m-1:
            res.append(1)
        if i == n-1:
            res.append(2)
        if j == 0:
            res.append(3)

        return res

    def get_next(i, j, heading):
        cur = grid[i][j]

        nxt_h = None
        if cur == 'S':
            nxt_h = heading
            if nxt_h == 0:
                i = i+1
            elif nxt_h == 1:
                j = j-1
            elif nxt_h == 2:
                i = i-1
            else:
                j = j+1
        elif cur == 'L':
            if heading == 0:
                j += 1
                nxt_h = 3
            elif heading == 1:
                i += 1
                nxt_h = 0
            elif heading == 2:
                j -= 1
                nxt_h = 1
            else:
                i -= 1
                nxt_h = 2
        elif cur == 'R':
            if heading == 0:
                j -= 1
                nxt_h = 1
            elif heading == 1:
                i -= 1
                nxt_h = 2
            elif heading == 2:
                j += 1
                nxt_h = 3
            else:
                i += 1
                nxt_h = 0

        if i < 0: i = n-1
        elif i >= n: i = 0

        if j < 0: j = m-1
        elif j >= m: j = 0

        return i, j, nxt_h

    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            starts = [0, 1, 2, 3]
            for heading in starts:
                if not visited[i][j][heading]:
                    h = 0
                    s = [heading, i, j]
                    x, y = i, j
                    while 1:
                        visited[x][y][heading] = True
                        h += 1
                        x, y, heading = get_next(x, y, heading)
                        if s == [heading, x, y]:
                            break
                    answer.append(h)
    answer = sorted(answer)
    return answer

grid = ["SLRLLRSSR","SLSLRSSSR", 'SLLRSRLLR', 'LRLRSRRRS']
print(solution(grid))
