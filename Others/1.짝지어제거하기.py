s = 'baabaa'
s = 'cdcd'
# s = 'baaccbbba'

from collections import deque

def solution(s):
    que = deque([])

    for i in s:
        if not que:
            que.append(i)
        
        elif que[-1] == i:
            que.pop()
        
        else:
            que.append(i)

    if que:
        answer = 0
    else:
        answer = 1
    
    return answer

print(solution(s))