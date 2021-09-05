# 시간초 실패
def convert(x):
    a, b, c = map(int, x.split(':'))
    return 3600*a+60*b+c

def deconvert(x):
    a = x//3600
    x -= a*3600
    b = x//60
    x -= b*60
    
    a = str(a).zfill(2)
    b = str(b).zfill(2)
    c = str(x).zfill(2)
    return a+':'+b+':'+c

def solution(play_time, adv_time, logs):
    answer = ''
    play = convert(play_time)
    arr = [0 for _ in range(play+1)]
    for log in logs:
        s, e = map(convert, log.split('-'))
        for i in range(s, e):
            arr[i] += 1

    adv = convert(adv_time)

    s = sum(arr[:adv])
    best = s
    loc = -1
    for i in range(0, play-adv):
        s = s - arr[i] + arr[i+adv]
        if best < s:
            best = s
            loc = i

    answer = deconvert(loc+1)
    print(answer)
    return answer

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

solution(play_time, adv_time, logs)