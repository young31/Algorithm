def make_table(s):
    n = len(s)
    table = [0 for _ in range(n)]
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = table[j-1]
        if s[i] == s[j]:
            j += 1
            table[i] = j
    return table

def KMP(s, p):
    table = make_table(p)
    n = len(s)
    len_p = len(p)
    cnt = 0
    j = 0
    answer = []

    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == p[j]:
            if j == len_p-1:
                cnt += 1
                answer.append(i-len_p+2)
                j = table[j]
            else:
                j += 1
    return answer, cnt

# def KMP(target, pattern):
#     table = make_table(pattern)
#     len_p = len(pattern)
#     n = len(target)
#     dist = 0 # 탐색지점
#     while 1:
#         idx = 0 # 길이
#         if idx+dist+len_p > n: # 길어지면 가망 없음
#             break
        
#         k = 0 # 일치 갯수
#         while target[idx+dist] == pattern[k]:
#             k += 1
#             idx += 1

#             if k == len_p: # 전부 일치
#                 answer.append(dist+1)
#                 break
        
#         dist = dist + (k - table[k])
#         k = 0

target = input()
pattern = input()

answer, cnt = KMP(target, pattern)
print(cnt)
for a in answer:
    print(a)