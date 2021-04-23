

def solution(brown, yellow):
    answer = []
    b = 1
    while 1:
        a = (brown + yellow)/b
        if (a-2)*(b-2) == yellow:
            return [a, b]
        else:
            b += 1
    return answer