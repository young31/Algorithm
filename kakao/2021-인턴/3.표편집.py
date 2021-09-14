def solution(n, k, cmd):
    removed = []
    adj = [[max(0, i-1), min(n-1, i+1)] for i in range(n)]
    for c in cmd:
        if len(c) >= 2:
            direction, step = c.split(' ')
            step = int(step)
            if direction == 'D':
                loc = 1
            else:
                loc = 0

            for _ in range(step):
                k = adj[k][loc]
                if k == 0 and loc == 0:
                    break
                elif k == n-1 and loc == 1:
                    break
        else:
            if c == 'Z':
                l = removed.pop()
                if adj[l][0] != l:
                    adj[adj[l][0]][1] = l
                if adj[l][1] != l:
                    adj[adj[l][1]][0] = l
            else:
                removed.append(k)
                if adj[k][1] == k:
                    adj[adj[k][0]][1] = adj[k][0]
                    k = adj[k][0]
                else:
                    adj[adj[k][0]][1] = adj[k][1]
                    adj[adj[k][1]][0] = adj[k][0]
                    k = adj[k][1]

    answer = ['O' for _ in range(n)]
    for x in removed:
        answer[x] = 'X'
    answer = ''.join(answer)
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

print(solution(n, k, cmd))