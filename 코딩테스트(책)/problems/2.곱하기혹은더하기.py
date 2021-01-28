# input
letter = '02984'

# answer: 576

# algo
## 처음이 0이거나 연산해야할 수가 0또는 1인 경우는 더하기를 해야하고 나머지는 곱해줘야 커짐
res = int(letter[0])
for l in letter:
    if res == 0 or l in '01':
        res += int(l)
    else:
        res *= int(l)

print(res)