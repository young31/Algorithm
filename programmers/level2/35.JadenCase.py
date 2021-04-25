s = "3people unFollowed me"	
s = "for the last week"
s = "11 1ser 2cnt cnt"
s = "123123ss"
s = "1 w e 1s"
s = "1 we11"
s = "w"

def rule(s):
    if s == "":
        return s
    try:
        int(s[0])
        return s.lower()
    except:
        s = s.lower()
        s0 = s[0].upper()
        return s0+s[1:]

def solution(s):
    answer = ' '
    print(s.split(' '))
    # print(ord(s.split(' ')[0]))
    res = list(map(rule, s.split(' ')))
    answer = answer.join(res)
    print(answer)
    return answer

solution(s)