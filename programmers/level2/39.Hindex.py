citations = [12, 11, 10, 9, 8, 1]
citations = [6, 6, 6, 6, 6, 1]
citations = [22, 42]

# 문제 설명이 충분하지 않아서 혼란스러웠던 문제

from collections import Counter

def solution(citations):
    answer = 0
    memo = {}
    citations = sorted(citations)
    m = min(citations)
    n = len(citations)
    m = min(n, m)

    count = Counter(citations)
    i = n
    while i > 0:
        print(i, m)
        if m in citations:
            i -= count[m]

        if i <= m:
            answer = m
            break

        m += 1
    print(answer)

    return answer


solution(citations)