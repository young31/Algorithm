N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4


def solution(N, road, K):
    inf = int(1e9)
    dist = [[inf]*N for _ in range(N)]

    for a, b, c in road:
        dist[a-1][b-1] = min(dist[a-1][b-1], c)
        dist[b-1][a-1] = min(dist[a-1][b-1], c)

    for i in range(N):
        dist[i][i] = 0

    print(dist)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

    print(dist[0])
    answer = len(list(filter(lambda x: x<=K, dist[0])))
    print(answer)
    return answer


solution(N, road, K)