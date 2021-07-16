s = ")()("
s = "(())()"	

from collections import deque

def solution(s):
    answer = True

    if s[0] ==')':
        return False

    que = deque([s[0]])
    for i in s[1:]:
        if not que:
            if i==')':
                return False
            else:
                que.append(i)
            continue
        
        if que[-1] == '(':
            if i == ')':
                que.pop()
            else:
                que.append(i)

    if not que:
        return True
    return False

print(solution(s))