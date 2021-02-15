# https://programmers.co.kr/learn/courses/30/lessons/60058
# input
in1 = '(()())()'
in2 = ')('
in3 = '()))((()'
# answer: 

# algo
def reverse(x):
    ans = ''
    for let in x:
        if let == '(':
            ans += ')'
        else:
            ans += '('
    return ans
    
def split(x):
    cnt = 0
    for i, let in enumerate(x):
        if let == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return x[:i+1], x[i++1:]

def correct(x):
    ans = reverse(x)
    ans = '(' + ans[1:-1] + ')'
    return ans

def is_correct(x):
    cnt = 0
    for let in x:
        if let == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True

def solution(p):
    if p == '':
        return p
    a, b = split(p)

    if is_correct(a):
        answer = a + solution(b)
    else:
        answer = '('
        answer += solution(b)
        answer += ')'
        answer += correct(a)[1:-1]

    return answer

print(solution(in1))
print(solution(in2))
print(solution(in3))