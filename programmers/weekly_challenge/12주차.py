def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    def dfs(k, used, c):
        nonlocal answer
        
        for i in range(n):
            if not used[i] and k >= dungeons[i][0]:
                used[i] = True
                dfs(k-dungeons[i][1], used, c+1)
                used[i] = False
        else:
            answer = max(c, answer)
            return

    used = [False for _ in range(n)]
    dfs(k, used, 0)
    print(answer)
    return answer

k = 80
dungeons = 	[[80,20],[50,40],[30,10]]
solution(k, dungeons)