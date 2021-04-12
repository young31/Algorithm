s = "abcdcba"
# s = "abacde"
s = "ABCCBA"

def check(s, i):
    n = len(s)
    answer = 0
    j = 1
    while 1:
        if i-j < 0 or i+j >= n:
            break
        if s[i-j] == s[i+j]:
            answer += 2
            j += 1
        else:
            break
    return answer+1

def check2(s, i1, i2):
    n = len(s)
    answer = 0
    j = 1
    while 1:
        if i1-j < 0 or i2+j >= n:
            break
        if s[i1-j] == s[i2+j]:
            answer += 2
            j += 1
        else:
            break

    return answer+2

def solution(s):
    answer = 1
    n = len(s)
    if n == 1:
        return 1
    for i in range(1, n):
        a = check(s, i)
        if answer < a:
            answer = a
        if s[i] == s[i-1]:
            a = check2(s, i-1, i)
            if answer < a:
                answer = a
        if i+1 < n and s[i] == s[i+1]:
            a = check2(s, i, i+1)
            if answer < a:
                answer = a

    return answer

print(solution(s))