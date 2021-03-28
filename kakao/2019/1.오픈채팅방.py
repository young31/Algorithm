# input
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

# answer: ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# algo
def solution(record):
    ids = {}
    tmp_ans = []

    for rec in record:
        words = rec.split(' ')
        if len(words) == 3: # enter / change
            if words[0] == 'Enter':
                ids[words[1]] = words[2]
                # msg = f'{ids[words[1]]}님이 들어왔습니다.'
                tmp_ans.append(('enter', words[1]))
            else: # change
                ids[words[1]] = words[2]
        elif len(words) == 2: # leave
            # msg = f'{ids[words[1]]}님이 나갔습니다.'
            tmp_ans.append(('leave', words[1]))

    answer = []
    for ans in tmp_ans:
        t, i = ans
        if t == 'enter':
            msg = f"{ids[i]}님이 들어왔습니다."
        else:
            msg = f"{ids[i]}님이 나갔습니다."
        answer.append(msg)

    return answer

print(solution(record))