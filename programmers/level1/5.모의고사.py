answers = [1,2,3,4,5]


def solution(answers):
    answer = []
    n = len(answers)
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]

    ans1 = a1*(n//len(a1)) + a1[:n%len(a1)]
    ans2 = a2*(n//len(a2)) + a2[:n%len(a2)]
    ans3 = a3*(n//len(a3)) + a3[:n%len(a3)]

    scores = [0, 0, 0]
    for a, a1, a2, a3 in zip(answers, ans1, ans2, ans3):
        if a==a1:
            scores[0] += 1
        if a==a2:
            scores[1] += 1
        if a==a3:
            scores[2] += 1

    m = max(scores)
    for i, s in enumerate(scores):
        if s == m:
            answer.append(i+1)
    print(answer)
    return answer

solution(answers)