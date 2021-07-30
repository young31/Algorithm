n = int(input())


check_col = [False] * (n*2+1); check_d1 = [False] * (n*2+1); check_d2 = [False] * (n*2+1)
def process(row):
    answer = 0
    if row == n+1:
        return 1
    for i in range(1,n+1):
        d1 = row+i; d2 = n + (row - i)
        if check_col[i] == False and check_d1[d1] == False and check_d2[d2] == False:
            check_col[i] = True; check_d1[d1] = True; check_d2[d2] = True
            answer += process(row+1)
            check_col[i] = False; check_d1[d1] = False; check_d2[d2] = False
    return answer
answer = process(1)
print(answer)