s = "-1 -2 -3 -4"

def solution(s):
    answer = ''
    a = list(map(lambda x: int(x), s.split(' ')))
    answer = f'{min(a)} {max(a)}'
    print(answer)
    return answer

solution(s)