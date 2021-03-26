# input
str1 = 'aa1+aa2'
str2 = 'AAAA12'

# answer: 43960

# algo
def check(x):
    a, b = x
    if ord(a) < ord('a') or ord(a) > ord('z') or ord(b) < ord('a') or ord(b) > ord('z'):
        return False
    return True

def prepocessing(x):
    x = x.lower()
    x_set = []
    for i in range(len(x)-1):
        if check(x[i:i+2]):
            x_set.append(x[i:i+2]) 
    return x_set

def solution(str1, str2):
    set1 = prepocessing(str1)
    set2 = prepocessing(str2)

    inter = []
    for s in set1:
        if s in set2:
            set2.remove(s)
            inter.append(s)
    for i in inter:
        set1.remove(i)
    
    sums = len(set1) + len(set2) + len(inter)
    if sums == 0:
        print(65536)
        return 65536
    else:
        res = len(inter) / sums * 65536
        print(int(res))
        return int(res)

solution(str1, str2)