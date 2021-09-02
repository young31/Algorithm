table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

def solution(table, languages, preference):
    answer = ''
    scores = []

    for target in table:
        score = 0
        target_cri = target.split(' ')
        code = target_cri[0]
        for lang, pref in zip(languages, preference):
            try:
                score += (6 - target_cri.index(lang))*pref
            except:
                continue
        scores.append((-score, code))
    answer = sorted(scores)
    print(answer)
    answer = answer[0][1]
    return answer

solution(table, languages, preference)