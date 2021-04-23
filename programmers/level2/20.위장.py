clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

from collections import defaultdict

def solution(clothes):
    answer = 1
    dct = defaultdict(int)
    for a, b in clothes:
        dct[b] += 1

    for k, v in dct.items():
        answer *= (v+1)
    answer -= 1
    print(answer)
    return answer

solution(clothes)