def solution(word):
    answer = 0
    done = False
    def dfs(s):
        nonlocal answer, done
        if done:
            return
        if s == word:
            done = True
            return
        for w in ['A', 'E', 'I', 'O', 'U']:
            if len(s+w) <= 5:
                if not done:
                    answer += 1
                dfs(s+w)

    dfs('')
    return answer

word = 'EIO'
print(solution(word))