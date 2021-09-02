from collections import deque, defaultdict

n, k = map(int, input().split())
max_ = max(n, k)*4+1

def find(n, k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return min(find(n, k-1), find(n, k+1)) + 1
    else:
        return min(k-n, find(n, k//2) + 1)
        
# sol 2
# n, k = map(int, input().split())
# max_ = max(n, k)*4+1

# que = deque()
# que.append((n, 0))
# visited = defaultdict(bool)

# while que:
#     cur, c = que.popleft()
#     if cur == k:
#         print(c)
#         break
#     if not visited[cur-1]:
#         if cur-1 == k:
#             print(c+1)
#             break
#         que.append((cur-1, c+1))
#         visited[cur-1] = True
#     if not visited[cur+1] and cur+1 <= max_:
#         if cur+1 == k:
#             print(c+1)
#             break
#         que.append((cur+1, c+1))
#         visited[cur+1] = True
#     if not visited[cur*2] and cur*2 <= max_:
#         if cur*2 == k:
#             print(c+1)
#             break
#         que.append((cur*2, c+1))
#         visited[cur*2] = True