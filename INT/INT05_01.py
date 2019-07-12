# young
def eval_(a,b,c):
    a=int(a)
    b=int(b)
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '/':
        return round(a/b)
    else:
        return a*b

pro = ('+', '-', '/', '*')
for i in range(1, int(input()) + 1):
    t = list(input().split())
    j = 0
    try:
        while t[1] != '.':
            if t[j] in pro:
                re = eval_(t[j - 2], t[j-1], t[j])
                t.insert(j + 1, re)
                for k in range(3):
                    t.pop(j - 2)
                j -= 2
            else: j += 1
    except:
        t[0] = 'error'
    print('#%d'%i, t[0])