s = "[](){}"
# s = "[(])"

from collections import deque

def check(strs):
    c1 = ['{', '[', '(']
    c2 = ['}', ']', ')']
    if not strs:
        return True

    if strs[0] in c2:
        return False
    
    que = deque([strs[0]])
    for red in strs[1:]:
        if not que:
            if red in c2:
                return False
            else:
                que.append(red)
                continue 

        if que[-1] in c1:
            if ord(red)-ord(que[-1]) in [1, 2]:
                que.pop()
            else:
                que.append(red)
        
    if not que:
        return True
    else:
        return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        new = s[i:] + s[:i]
        res = check(new)
        
        if res:
            answer += 1
        print(new, res)
    print(answer)
    return answer

solution(s)
