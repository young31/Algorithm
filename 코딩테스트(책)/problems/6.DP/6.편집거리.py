# input
a1, b1 = 'cat', 'cut'
a2, b2 = 'sunday', 'saturday'
# answer: 1, 3

# algo
## DP로 해결하는 것이 와닿지는 않는다.. 나중에 더 생각해보기
def solution(a, b):
    table = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

    for i in range(len(a)+1):
        table[0][i] = i

    for i in range(len(b)+1):
        table[i][0] = i

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                table[j][i] = table[j-1][i-1]
            else:
                table[j][i] = 1 + min(table[j-1][i-1], table[j-1][i], table[j][i-1])


    print(table[j][i])

solution(a1, b1)
solution(a2, b2)