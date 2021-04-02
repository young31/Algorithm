# input
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"	

# answer: [2, 1, 3, 4]

# algo
def parsing(s):
    exclude = ['{', '}', ',']
    res = []
    tmp = ''
    flag = False
    for i in range(1, len(s)-1):
        if s[i] == '{':
            flag = True
        elif s[i] == '}':
            flag = False
            res.append(list(map(int, tmp.split(','))))
            tmp = ''

        if flag and s[i] != '{':
            tmp += s[i]

    return res

def solution(s):
    answer = []

    s = parsing(s)
    s = sorted(s, key=lambda x: len(x))

    for x in s:
        nxt = set(x) - set(answer)
        answer.append(list(nxt)[0])

    return answer


print(solution(s))