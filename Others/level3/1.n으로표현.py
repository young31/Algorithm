N = 4
number = 17

def operations(n, N):
    res = [
        n+N, n-N, n*N, N-N
    ]
    if n != 0:
        res.append(N//n)
    elif N != 0:
        res.append(n//N)

    for r in res:
        yield abs(r)

def solution(N, number):
    if N == number:
        return 1
    trials = [set([N])]

    for answer in range(2, 9):
        nn = int(str(N)*answer)
        if nn == number:
            return answer
        trials.append(set([nn]))

        for i in range(1, answer//2+1):
            j = answer - i

            for x in (trials[i-1]):
                for y in (trials[j-1]):
                    for tmp in operations(x, y):
                        if tmp == number:
                            return answer
                        else:
                            trials[-1].add(tmp)

    return -1

print(solution(N, number))