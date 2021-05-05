new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "z-+.^."
new_id = "=.="
new_id = "123_.def"
new_id = "abcdefghijklmn.p"

import re

def remove(strs, start=True, end=True):
    if start and strs[0] == '.':
        if len(strs) == 1:
            return ''
        strs = strs[1:]
    
    if end and strs[-1] == '.':
        if len(strs) == 1:
            return ''
        strs = strs[:-1]
    
    return strs
        

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    print(new_id)
    new_id = ''.join(re.findall(r'[a-z|\d|\-|\_|\.]+', new_id))
    print(new_id)
    new_id = re.sub(r'[.]+', '.', new_id)
    print(new_id)
    new_id = remove(new_id)
    
    if new_id == '':
        new_id = 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = remove(new_id, False, True)

    if len(new_id) <= 2:
        new_id += new_id[-1]*(3-len(new_id))

    print(new_id)
    return new_id

solution(new_id)