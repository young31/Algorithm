begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


from collections import deque

def is_match(x, target):
    dif = 0
    for a, b in zip(x, target):
        if a != b:
            dif += 1
        if dif > 1:
            return False
    if dif == 1:
        return True

def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    n = len(words)
    que = deque([(begin, 0)])
    visited = [False] * n

    while que:
        print(que)
        cur, answer = que.popleft()
        for i, w in enumerate(words):
            if not visited[i] and is_match(cur, w):
                if w == target:
                    return answer+1
                que.append((w, answer+1))

    return 0


print(solution(begin, target, words))