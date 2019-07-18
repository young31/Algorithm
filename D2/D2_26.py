# young 24142ms, 494
N = int(input())
 
for i in range(1,N+1) :
    n = int(input())
    for j in range(0,n) :
        set_ = list(map(int,input().split( )))
        if set_[0] == max(set_) :
            print("#{} {}".format(i, 0))
            break
        else :
            t = 0
            while len(set_) > 1 :
                max1 = set_.index(max(set_))
                t += max(set_) * max1 - sum(set_[0:max1])
                set_ = set_[max1+1:]
            print("#{} {}".format(i,t))
            break