participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

from collections import defaultdict

def solution(participant, completion):
    answer = ''
    people = defaultdict(int)

    for p in participant:
        people[p] += 1

    for c in completion:
        people[c] -= 1

    for name, cnt in people.items():
        if cnt == 1:
            answer += name

    return answer

solution(participant, completion)