n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

# n = 5
# words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

# n = 2
# words = ["hello", "one", "even", "never", "now", "world", "draw"]

import math

def solution(n, words):
    answer = []
    used = []
    flag = False
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            flag = True
            break
        elif words[i] in words[:i]:
            flag = True
            break

    if flag:
        i += 1
        ith = n if i%n == 0 else i%n
        answer = [ith, math.ceil(i/n)]
    else:
        answer = [0, 0]

    print(answer)
    return answer

solution(n, words)