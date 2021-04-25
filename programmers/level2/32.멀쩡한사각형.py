w = 8
h = 12

# 기존 방식으로는 시간초과 문제 발생
## => 최대공약수와 관련이 있다는 내용을 참조하여 통과...(생각보다 난이도 높은 문제였다ㅠ)
def solution(w,h):
    if w == 1 or h == 1:
        return 0
    answer = 1
    i = j = 1

    k = 1
    pre = h/w
    while 1:
        c = i*pre
        if c < j:
            step = int(1/c)+1
            answer += step
            i += step
            print(step, i, j)
        elif c > j:
            step = int(1/c)+1
            answer += step
            j += step
            print(step, i, j)
        else:
            k = w//i
            break

        if i == w and h == j:
            break

    answer = w*h - answer*k
    print(answer, k)
    return answer


def search(a, b):
    m = min(a, b)
    for i in range(m, 0, -1):
        if a%i == 0 and b%i == 0:
            return i

def solution(w,h):
    answer = w*h - w - h + search(w, h)
    print(answer)
    return answer

solution(w, h)