import random

for _ in range(10):
    a1 = random.randint(2, 10000)
    a2 = random.randint(2, 10000)
    n = max(a1, a2)
    m = min(a1, a2)
    print(n, m)

    t = 0
    while 1:
        max_ = (n//m)*m
        t += (n-max_)
        n = max_
        if n == 0:
            t -= 1
            break
        n /= m
        t += 1
        # input()
        if n == 1:
            break
    print(t)
    print()