def solution(s):
    answer = ''.join(sorted(s, key=lambda x: -ord(x)))
    return answer