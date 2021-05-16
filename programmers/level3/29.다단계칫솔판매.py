enroll =  ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]


def solution(enroll, referral, seller, amount):
    answer = []

    tree = {}
    ben = {}
    for e, r in zip(enroll, referral):
        tree[e] = r
        ben[e] = 0

    for s, a in zip(seller, amount):
        amt = 100*a
        e = tree[s]
        while 1:
            tax = amt//10 if amt*0.1 != 0 else amt//10+1
            ben[s] += (amt - tax)
            
            if e == '-' or amt < 10:
                break
            s = e
            e = tree[s]
            amt = tax

    answer = list(ben.values())
    return answer


solution(enroll, referral, seller, amount)