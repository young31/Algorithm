number = "4177252841"
k = 4

# number = "7777"
# k = 1


def solution(number, k):
    answer = ''
    number = list(map(int, number))

    removed = []
    for i in range(len(number)-1):
        if number[i+1] > number[i]:
            removed.append(i)
            if len(removed) == k:
                new = [str(number[i]) for i in range(len(number)) if i not in removed]
                answer = answer.join(new)
                print(removed)
                return answer

            for j in range(i-1, -1, -1):
                
                if number[j] < number[i+1] and j not in removed:
                    removed.append(j)
                else:
                    break
                
                if len(removed) == k:
                    new = [str(number[i]) for i in range(len(number)) if i not in removed]
                    answer = answer.join(new)
                    print(removed)
                    return answer

    new = [number[i] for i in range(len(number)) if i not in removed]
    while len(removed) <= k:
        m = min(new)
        new.remove(m)
    new = list(map(str, new))
    answer = answer.join(new)
    return answer


# print(solution(number, k))


def solution(number, k):
    answer = ''
    number = list(map(int, number))

    for _ in range(k):
        for i in range(len(number)-1):
            if number[i+1] > number[i]:
                number.pop(i)
                break
        else:
            m = min(number)
            number.remove(m)

    number = list(map(str, number))
    answer = answer.join(number)
    return answer


def solution(number, k):
    answer = ''
    number = list(map(int, number))
    n = len(number)
    new = []

    cnt = 0
    i = 0
    j = 1
    while i < n:
        if not new:
            new.append(number[i])
            i += 1
            continue
        else:
            if new[-1] < number[i]:
                new.pop()
                cnt += 1
            else:
                new.append(number[i])
                i += 1

        if cnt == k:
            break
        
    print(k, cnt)
    fin = list(map(str, new+number[i:]))
    fin = fin[:len(fin)-k+cnt]
    print(fin)
    answer = answer.join(fin)

    return answer

print(solution(number, k))