n = int(input())
cnt = 0
cand = [(n, cnt)]
continued = True if n != 1 else False

while continued:
    for ca, cnt in cand:
        if ca%3 == 0:
            if ca//3 == 1:
                continued = False
                cnt += 1
                break
            cand.append((ca//3, cnt+1))

        if ca%2 == 0:
            if ca//2 == 1:
                continued = False
                cnt += 1
                break
            cand.append((ca//2, cnt+1))
        
        if ca-1 == 1:
            continued = False
            cnt += 1
            break
        else:
            cand.append((ca-1, cnt+1))

print(cnt)