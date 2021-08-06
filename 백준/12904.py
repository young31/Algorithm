s = input()
t = input()

while 1:
    if t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    else:
        t = t[:-1]

    if len(t) == len(s):
        if t == s:
            print(1)
        else:
            print(0)
        break