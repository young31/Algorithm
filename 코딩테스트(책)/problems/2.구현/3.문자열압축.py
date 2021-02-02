# https://programmers.co.kr/learn/courses/30/lessons/60057
# input
ex1 = 'aabbaccc'
ex2 = 'ababcdcdababcdcd'
ex3 = 'abcabcdede'
ex4 = 'abcabcabcabcdededededede'
ex5 = 'xababcdcdababcdcd'
# answer: 7, 9, 8, 14, 17

# algo
def solution(s):
    # 초기화; 반으로 짤랐을 때 까지만 확인해 봄
    max_len = len(s)//2+1
    min_length = len(s)

    for term in range(1, max_len):
        ans = ''
        FlAG = False # 압축이 가능한 지(이전과 같은 지)
        prev = s[0:term]
        cnt = 1
        for i in range(term, len(s), term): # 처음 부터 해당 길이로 무조건 나누어져야 한다는 조건이 있음
            nxt = s[i:i+term]
            if prev == nxt:
                FLAG = True
            else:
                FLAG = False

            if not FLAG:
                if cnt == 1: # 바로 다른 것이면 1은 작성하지 않음
                    ans += (prev)
                else:
                    ans += (str(cnt)+prev)
                cnt = 1

            else:
                cnt += 1

            prev = nxt

        if cnt == 1:
            ans += (prev)
        else:
            ans += (str(cnt)+prev)

        if len(ans) < min_length:
            min_length = len(ans)

    return min_length


print(solution(ex5))