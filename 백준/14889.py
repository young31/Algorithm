from itertools import combinations
import sys

def get_score(arr, team):
    score = 0
    for a, b in combinations(team, 2):
        score += arr[a][b] + arr[b][a]
    return score

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

best_score = float('inf')

for comb in combinations(range(n), n//2):
    sA = get_score(arr, comb)
    sB = get_score(arr, list(filter(lambda x: x not in comb, range(n))))
    s = abs(sA - sB)
    if s < best_score:
        best_score = s

print(best_score)