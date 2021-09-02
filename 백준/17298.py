n = int(input())
arr = list(map(int, input().split()))

answer = [-1]
stack = [arr[-1]]

for r in arr[::-1][1:]:
    if r < stack[-1]:
        answer += [stack[-1]]
        stack.append(r)
    else:
        while 1:
            a = stack.pop()
            if a > r:
                answer += [a]
                stack.append(a)
                stack.append(r)
                break
            
            if not stack:
                answer += [-1]
                stack += [r]
                break
        
print(*answer[::-1])