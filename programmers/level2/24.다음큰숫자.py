n = 15

def binarize(n):
    res = []
    i = 1
    while n > 0:
        k = n%(2**i)
        res.append(k//(2**(i-1)))
        n -= res[-1]*(2**(i-1))
        i += 1

    return res

def rev_bin(arr):
    ans = 0
    for i, n in enumerate(arr):
        ans += n*(2**i)
    return ans

# print(rev_bin(binarize(15)))

# def solution(n):
#     answer = 0

#     n = binarize(n)
#     print(n)
#     a = n.index(1)
#     if 0 in n:
#         b = n.index(0, a)
#         n[a], n[b] = n[b], n[a]
#     else:
#         n[-1] = 0
#         n.append(1)
#     print(n)
#     answer = rev_bin(n)
#     print(answer)
#     return answer


def solution(n):
    answer = 0

    ones = bin(n).count('1')

    n += 1
    while 1:
        if bin(n).count('1') == ones:
            answer = n
            break
        n += 1
    print(answer)
    return answer

solution(78)
