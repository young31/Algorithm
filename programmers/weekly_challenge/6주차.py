def solution(weights, head2head):
    n = len(weights)
    scores = [[0, 0, -weights[i], i+1] for i in range(n)]
    games = [0 for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if head2head[i][j] == 'W':
                scores[i][0] -= 1
                if weights[j] > weights[i]:
                    scores[i][1] -= 1
            if head2head[i][j] != 'N':
                games[i] += 1
                
    for i in range(n):
        if games[i] != 0:
            scores[i][0] /= games[i]
            
    scores.sort()
    answer = [x[-1] for x in scores]
    
    return answer