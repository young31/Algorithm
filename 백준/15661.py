from itertools import combinations

def get_score(team, mat):
    score = 0
    for a, b in combinations(team, 2):
        score += mat[a][b] + mat[b][a]
    return score


n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

best_score = float('inf')
for k in range(1, n//2+1):
    for ta in combinations(range(n), k):
        tb = list(filter(lambda x: x not in ta, range(n)))
        sa = get_score(ta, mat)
        sb = get_score(tb, mat)
        if abs(sa - sb) < best_score:
            best_score = abs(sa - sb)
print(best_score)
