skill = "CBD"
skill_trees = ["C", "D", "CB", "BDA"]

def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        NOT = False
        idx = -1
        for s in skill:
            try:
                i = st.index(s)
            except:
                i = len(st)
            if idx < i or i==len(st):
                idx = i
                continue
            else:
                NOT = True
                break
        
        if not NOT:
            answer += 1

    print(answer)
    return answer

solution(skill, skill_trees)