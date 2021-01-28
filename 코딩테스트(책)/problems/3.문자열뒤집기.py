# input
letter =  '0001100'
# answer: 1

# algo
## 0, 1에대해서 연속하는 그룹의 수를 찾고 그 중 작은 값을 뒤집으면 최소가 됨
zeros = 0
ones = 0
start = letter[0]
if start == '0':
    zeros += 1
else:
    ones += 1

for l in letter[1:]:
    if start == l:
        start = l
    else:
        if l == '0':
            zeros += 1
        else:
            ones += 1

print(zeros, ones)
print(min(zeros, ones))