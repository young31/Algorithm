a = '1S2D*3T'
b = '1D2S#10S'

def find_idx(letter):
    i = -1
    for i in range(2, len(letter)):
        try:
            int(letter[i])
            break
        except:
            continue
    if i == -1:
        i = len(letter)+1
    return i

def compute(x):
    x.reverse()
    # print(x)
    ans = 0
    n = x[0]**x[1]
    if len(x) == 2:
        return n
    else:
        n *= x[-1]
        return n


def solution(dartResult):
    answer = 0

    ans = [0, 0, 0]

    for t in range(3):
        fi = find_idx(dartResult)
        if t == 2:
            fi += 1
        fl = dartResult[:fi]
        dartResult = dartResult[fi:]

        fl = fl[::-1]
        tmp = []
        for idx in range(len(fl)):
            i = fl[idx]
            if i == '#':
                tmp.append(-1)
            elif i == '*':
                tmp.append(2)
                if t > 0:
                    ans[t-1] *= 2
            elif i == 'S':
                tmp.append(1)
            elif i == 'D':
                tmp.append(2)
            elif i == 'T':
                tmp.append(3)
            else:
                n = fl[idx:]
                n = n[::-1]
                n = int(n)
                tmp.append(n)
                break
        ans[t] = compute(tmp)

    return sum(ans)
