# young 119ms, 329
T = int(input())
 
for i in range(1,T+1) :
    l = list(input())
    y = int("".join(l[0:4])) ; m = float("".join(l[4:6])) ; d = float("".join(l[6:8]))
    if d < 1 or m < 1 or (m == 2 and d > 28) or (m == 4 | 6 | 9 | 11 and d > 30) :
        print("#%d -1" % i)
    else :
        print("#%d %04.0f/%02.0f/%02.0f" % (i, y, m, d))
      

      
# jeong 123ms, 842
# respect young..

def check_m(month):
    result = False
    if (0 < month < 13):
        result = True
    return result
 
 
def check_d(month, day):
    result = False
     
    if month == 2:
        if 0 < day < 29:
            result = True
    elif month % 2 == 1:
        if (month < 8 and 0 < day < 32):
            result = True
        elif (month > 8 and 0 < day < 31):
            result = True
    else:
        if (month < 8 and 0 < day < 31):
            result = True
        elif (month > 8 and 0 < day < 32):
            result = True
 
    return result
 
 

T = int(input())
for i in range(T):
    date = input()
    month = int(date[4:6])
    day = int(date[6:])
    if (check_m(month) and check_d(month, day)):
        print('#{0} {1}/{2}/{3}'.format(i + 1, date[:4], date[4:6], date[6:]))
    else:
        print('#{0} -1'.format(i + 1))
