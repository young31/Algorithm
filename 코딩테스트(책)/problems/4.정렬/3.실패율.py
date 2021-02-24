# https://programmers.co.kr/learn/courses/30/lessons/42889
# input
n1 = 5
stages1 = [2, 1, 2, 6, 2, 4, 3, 3]

n2 = 4
stages2 = [4, 4, 4, 4, 4]
# answer: [3, 4, 2, 1, 5] / [4, 1, 2, 3]

# algo
def solution(n, stages):
    bins = [0 for _ in range(max(stages))]
    fr = {}

    for s in stages:
        bins[s-1] += 1

    for i in range(n):
        passing = sum(bins[i:])
        fr[i+1] = 0 if passing==0 else bins[i] / (sum(bins[i:]))

    # print(bins)
    # print(fr)
    # print(sorted(fr, key=lambda x: -fr[x]))

    return sorted(fr, key=lambda x: -fr[x])


    
solution(n1, stages1)
solution(n2, stages2)
