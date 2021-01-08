# input
n, k = 5, 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
# answer: 26

# algo
a_ = sorted(a)
b_ = sorted(b, reverse=True)

def main():
    cnt = 0
    while 1:
        for j in range(n):
            for l in range(n):
                if a_[j] < b_[l]:
                    a_[j], b_[l] = b_[l], a_[j]
                    cnt += 1
                    break
            if cnt == k:
                return a_

print(main())
print(sum(a_))
