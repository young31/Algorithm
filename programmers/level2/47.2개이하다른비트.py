numbers = [2, 7]

def solution(numbers):
    answer = []
    for num in numbers:
        bnum = list(bin(num)[2:])
        cnt = bnum.count('0')

        if cnt == 2:
            n = len(bnum)
            ans = int('1'*n, 2)
            answer.append(ans)
        elif cnt == 1:
            b = '1' + ''.join(bnum).replace('1', '0')
            answer.append(int(b, 2))
        elif cnt == 0:
            b = ['1', '0'] + bnum[1:]
            answer.append(int(''.join(b), 2))
    print(answer)
    return answer

solution(numbers)
