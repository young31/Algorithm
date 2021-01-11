# input
target = 26
# answer: 3

# algo
def step(x, target):
    if x*5 <= target:
        return x*5

    elif x*3 <= target:
        return x*3

    elif x*2 <= target:
        return x*2

    else:
        return x + 1

def main():
    n = 1
    t = 0
    while 1:
        n = step(n, target)
        t += 1
        if n == target:
            return t

print(main())


