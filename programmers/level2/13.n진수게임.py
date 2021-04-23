n=2; t=4; m=2; p=1
n=4; t=4; m=4; p=4
# n=2; t=2; m=100; p=100


import math

class Memory:
    def __init__(self, length):
        self.length = length
        self.memory = []
        self.prev = []

    def push(self, strs):
        for s in strs:
            self.memory.append(s)
            if len(self.memory) >= self.length:
                self.prev.append(self.memory)
                self.memory = []

def converter(n, k):
    global letters
    ans = ''
    if k < n:
        return letters[k]

    i = int(math.log(k, n)) # 부동소수점 오류발생하여 오답인 경우가 생김!!
    while 0 <= i:
        m = (n**i)
        ans += letters[k//m]
        k = k%m
        i -= 1
    return ans

def converter(n, k):
    global letters
    answer = ''
    if k == 0: return '0'
    while k > 0:
        answer = letters[k%n] + answer
        k = k//n
    return answer

def solution(n, t, m, p):
    global letters
    letters = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    p -= 1
    answer = ''
    memory = Memory(m)

    i = 0
    while 1:
        num = converter(n, i)
        memory.push(num)
        if len(memory.prev) >= t:
            break
        i += 1
    for rec in memory.prev[:t]:
        answer += rec[p]
    return answer

letters = None
solution(n, t, m, p)