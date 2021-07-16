rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

from pprint import pprint

def rotate(i1, j1, i2, j2):
    for j in range(j1, j2+1):
        yield (i1, j)
    
    for i in range(i1+1, i2+1):
        yield (i, j)

    for j in range(j2-1, j1-1, -1):
        yield (i, j)

    for i in range(i2-1, i1, -1):
        yield (i, j)

# for k in rotate((2, 2), (5, 4)):
#     print(k)

def solution(rows, columns, queries):
    answer = []

    board = [list(range(1+i*columns, 1+i*columns+columns)) for i in range(rows)]
    
    for i1, j1, i2, j2 in queries:
        tmp_dct = {}
        tmp_arr = []
        min_ = float('inf')
        for i, j in rotate(i1-1, j1-1, i2-1, j2-1):
            v = board[i][j]
            tmp_dct[(i, j)] = v
            tmp_arr.append((i, j))
            if v < min_:
                min_ = v
        
        for k in range(len(tmp_arr)):
            i, j = tmp_arr[k]
            if k == len(tmp_arr)-1:
                ni, nj = tmp_arr[0]
            else:
                ni, nj = tmp_arr[k+1]

            board[ni][nj] = tmp_dct[(i, j)]

        pprint(board)
        answer.append(min_)
    print(answer)
    return answer

solution(rows, columns, queries)