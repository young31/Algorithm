msg = 'TOBEORNOTTOBEORTOBEORNOT'

class Message:
    def __init__(self):
        self.dct = {i: chr(i+64) for i in range(1, 27)}
        self.dct_inv = {chr(i+64): i for i in range(1, 27)}
        self.last_idx = 27

    def isin_chr(self, x):
        if x in self.dct_inv.keys():
            return True
        return False

    def push(self, x):
        self.dct_inv[x] = self.last_idx
        self.dct[self.last_idx] = x
        self.last_idx += 1

def solution(msg):
    message = Message()
    n = len(msg)
    answer = []
    msg += '/' # 문자열 종료 태그

    i = 0
    while i < n:
        for j in range(1, n+1):
            if not message.isin_chr(msg[i:i+j+1]):
                message.push(msg[i:i+j+1])
                answer.append(message.dct_inv[msg[i:i+j]])
                i += j
                break

    print(answer)
    return answer

solution(msg)