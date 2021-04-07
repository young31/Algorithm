s = "110010101001"

def make_binary(n):
    answer = ''
    while n:
        answer += str(n%2)
        n //= 2
        
    return answer
            

def solution(s):
    answer = []
    cnt = 0
    c = 0
    while s != '1':
        lens = len(s)
        s = s.replace('0', '')
        cnt += lens - len(s)
        n = len(s)
        s = make_binary(n)
        c += 1

    answer = [c, cnt]
    print(answer)
    return answer

solution(s)