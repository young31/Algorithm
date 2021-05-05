def solution(lottos, win_nums):
    answer = []
    removed_n = lottos.count(0)
    pre = set(win_nums).intersection(set(lottos))
    max_ = min(6, len(pre)+removed_n)
    min_ = len(pre)
    answer = [min(6, 7-max_), min(6, 7-min_)]
    return answer