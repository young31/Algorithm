m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

import re

def convert(x):
    c_map = {}
    for c in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        c_map[c+'#'] = c.lower()

    for i, v in c_map.items():
        x = x.replace(i, v)
    return x

def parsing(x):
    start, end, title, lyrics = x.split(',')
    s_0, s_1 = start.split(':')
    e_0, e_1 = end.split(':')
    start = int(s_0)*60+int(s_1)
    end = int(e_0)*60+int(e_1)

    dur = end-start
    lyrics = convert(lyrics)

    if dur < len(lyrics):
        return (lyrics[:dur], dur, title)
    else:
        m = dur // len(lyrics)
        # print(lyrics*m + lyrics[:dur-m*len(lyrics)], len(lyrics*m + lyrics[:dur-m*len(lyrics)]))
        return (lyrics*m + lyrics[:dur-m*len(lyrics)], dur, title)


def solution(m, musicinfos):
    answer = ''
    m = convert(m)

    res = sorted(musicinfos, key=lambda x: (0, -parsing(x)[1]) if re.search(m, parsing(x)[0]) is not None else (1, -parsing(x)[1]))
    # print(res)
    if re.search(m, parsing(res[0])[0]) is not None:
        return res[0].split(',')[2]

    return '(None)'

print(solution(m, musicinfos))