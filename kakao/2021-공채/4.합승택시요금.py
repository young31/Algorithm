def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    for i in range(n+1):
        graph[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    for i in range(1, n+1):
        answer = min(graph[s][i] + graph[i][a] + graph[i][b], answer)

    return answer


n = 6; s=4; a=6; b=2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n, s, a, b, fares)