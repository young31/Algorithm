# https://www.acmicpc.net/submit/10825/

n = int(input())
scores = []
for _ in range(n):
    scores.append(input().split())

res = sorted(scores, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for r in res:
    print(res[0])