n = int(input())
graph = [
    list(map(int, input().split())) for _ in range(n)
]

dp = [[None for _ in range(n)] for _ in range(1<<n)]

def find(loc=0, visited=1<<0):
    if visited == (1<<n)-1: # 전부 1이면
        return graph[loc][0] if graph[loc][0] != 0 else float('inf')
    
    if dp[visited][loc] is not None: # 방문 기록이 있으면
        return dp[visited][loc]

    cost = float('inf')
    for i in range(n):
        if visited&(1<<i) == 0 and graph[loc][i] != 0: # 방문하지 않았으면(해당 부분이 0이면)
            cost = min(cost, find(i, visited|(1<<i))+graph[loc][i]) # 가능한 값을 찾아서 최소 값 할당
    print(dp)
    dp[visited][loc] = cost
    return cost

res = find()
print(res)