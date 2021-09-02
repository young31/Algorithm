n, k = map(int, input().split())

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x]) 
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    
    parents[a] = b

arr = list(range(n))
parents = list(range(n))

answer = []
idx = 0
while len(answer) != n:
    p = find(parents, idx)
    for _ in range(k-1):
        p = find(parents, (p+1)%(n))
    union(parents, p, (p+1)%(n))
    idx = p
    answer.append(p+1)

print('<'+str(answer)[1:-1]+'>')