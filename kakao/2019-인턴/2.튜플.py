# solution 1
def parsing(s):
    ls = []
    flag = False
    for i in s:
        if i == '{':
            flag = True
            tmp = ''
            continue
        elif i == '}':
            flag = False
            ls.append(list(map(int, tmp.split(','))))
            continue
        if flag:
            tmp += i
    return ls

def solution(s):
    s = s[1:-1]
    ls = parsing(s)
    sort_key = {i: len(x) for i, x in enumerate(ls)}
    answer = []
    prev = None
    for k in sorted(sort_key.keys(), key=sort_key.get):
        if prev is None:
            answer.append(ls[k][0])
            prev = set(ls[k])
        else:
            answer.append(list(set(ls[k]) - prev)[0])
            prev = set(ls[k])
    return answer

# solution 2
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