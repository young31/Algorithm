# input
n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
# answer: "00:00"

# algo
def convert(time):
    a, b = time.split(':')
    res = int(a)*60 + int(b)
    return res

def de_convert(time):
    a = time//60
    b = time%60
    a = str(a)
    if len(a) == 1:
        a = '0' + a
    b = str(b)
    if len(b) == 1:
        b = '0' + b

    res = str(a) + ':' + str(b)
    return res

def cut_off(people, time, m):
    cnt = 0
    i = len(people)
    for i, p in enumerate(people):
        if p <= time:
            cnt += 1
        else:
            break

        if cnt == m:
            i += 1
            break
    
    return i
    

def solution(n, t, m, timetable):
    start = convert('09:00')
    bus = [start+t*i for i in range(n)]
    people = list(map(convert, timetable))
    people.sort()

    get_in = []
    for i in range(n):
        cut = cut_off(people, bus[i], m)
        get_in.append(people[:cut])
        people = people[cut:]
    
    target = get_in[-1]

    if len(target) < m:
        thres = bus[-1]
        print(de_convert(thres))
        return de_convert(thres)
    else:
        print(de_convert(max(target)-1))
        return de_convert(max(target)-1)

solution(n, t, m, timetable)