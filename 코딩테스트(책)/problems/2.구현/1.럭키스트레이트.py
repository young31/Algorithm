# input
ex1 = '123402'
ex2 = '7755'
# answer: LUCKY, READY

# algo
def sol(ex):
    mid = len(ex)//2
    score_l = 0
    score_r = 0

    for i in range(mid):
        score_l += int(ex[i])
        score_r += int(ex[i+mid])

    if score_l == score_r:
        return 'LUCKY'
    else:
        return 'READY'

print(sol(ex1))
print(sol(ex2))