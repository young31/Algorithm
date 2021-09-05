import re

def step2(s):
    o = ord(s)
    if ord('a') <= o <= ord('z'):
        return True
    elif ord('0') <= o <= ord('9'):
        return True
    elif s in ['.', '_', '-']:
        return True
    return False

def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join(list(filter(step2, list(new_id))))
    new_id = re.sub(r'[.]+', '.', new_id)

    if len(new_id) >= 1 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]

    if new_id == '':
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    if len(new_id) <= 2:
        new_id += new_id[-1]*(3-len(new_id))

    print(new_id)
    return new_id

new_id = 'abcdefghijklmn.p'
solution(new_id)