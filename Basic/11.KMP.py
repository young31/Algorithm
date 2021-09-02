# 문자열 매칭 판단 알고리즘
## 하나하나 확인하지 말고 겹치는 부분 끼리 점프해서 확인하자
## 이 때 겹치는 부분정도에 따라서 점프할 거리를 미리 계산(table)
## 백준: 1786
def make_table(s):
    n = len(s)
    table = [0 for _ in range(n)]
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = table[j-1]
        if s[i] == s[j]:
            j += 1
            table[i] = j
    return table

def KMP(s, p):
    table = make_table(p)
    n = len(s)
    len_p = len(p)
    j = 0

    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == p[j]:
            if j == len_p-1:
                j = table[j]
                print('find')
            else:
                j += 1

s = 'ABAABACABAACCABACABACABAACABACABAAC'
p = 'ABACABAAC'

KMP(s, p)