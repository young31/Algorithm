# young
#  {( }) 경우 예외 처리 추가해야함
for i in range(1, int(input()) + 1):
    l = list(input())
    s1 = []
    p = (40, 41, 123, 125)
    for let in l:
        if ord(let) in p:
            s1.append(let)
    n = 1
    for j in s1:
        try:
            if j == '(':
                s1.remove(')')
            elif j == '{':
                s1.remove('}')
            else:
                n = 0
                break
        except:
            n = 0
            break
    print('#%d'%i, n)