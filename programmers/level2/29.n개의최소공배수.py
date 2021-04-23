arr = [2,6,8,14]
# arr = [1,2,3]
# arr = [3,5,7,9]

def prime(k):
    res = [2, 3]
    for i in range(4, k+1):
        if not list(filter(lambda x: i%x == 0, res)):
            res.append(i)
    return res

def decompose(x, prime):
    res = [0]*len(prime)

    for i, p in enumerate(prime):
        if x%p == 0:
            res[i] = exponential(x, p)

    return res

def exponential(x, a):
    i = 0
    while 1:
        if x%a == 0:
            i += 1
            x //= a
        else:
            return i

def solution(arr):
    answer = 1
    m = max(arr)
    primes = prime(m)
    arr2 = [0]*len(primes)

    for a in arr:
        decomp = decompose(a, primes)
        arr2 = list(map(lambda x, y: max(x, y), arr2, decomp))

    for a, p in zip(arr2, primes):
        if a != 0:
            answer *= p**a
    print(answer)
    return answer

solution(arr)