# input
n = 5
group = [2, 3, 1, 2, 2]
# answer: 2

# algo
## 모든 모험가들이 포함될 필요는 없으므로 쉽게 해결 가능
## 가능한 많은 그룹을 만들기 위해서 공포도가 낮은 사람 기준으로 최소기준만 만족시키게 그룹을 생성
g = sorted(group)
n_group = 0
while 1:
    for i, c in enumerate(g):
        if i+1 >= c:
            n_group += 1
            g = g[i+1:]
            break
    else:
        break

print(n_group)