def solution(s):
    answer = True
    if len(s) not in [4, 6]:
        return False
    try:
        list(map(int, s))
        answer = True
    except:
        answer = False
    return answer