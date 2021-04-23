people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    answer = 0
    people.sort()
    l = 0
    r = len(people)-1
    c = 0
    while 1:
        print(c, l, r)
        if c + people[r] <= limit: # 큰 애 태우고 남는자리 있으면 작은 애로 눌러담기
            c += people[r]
            r -= 1

        elif c + people[l] <= limit:
            c += people[l]
            l += 1

        else:
            answer += 1
            c = 0

        if l == r: # 더 태울 수 없는 경우 남은 애를 태울 수 있으면 태우고 아니면 한 대 더 부름
            if c + people[l] <= limit:
                answer += 1
            else:
                answer += 2
            break
    print(answer)
    return answer

solution(people, limit)