def solution(scores):
    answer = ''
    n = len(scores)
    for i in range(n):
        tmp = [x[i] for x in scores]
        max_ = max(tmp)
        min_ = min(tmp)
        self_ = tmp[i]
        if self_==max_ and tmp.count(self_) == 1:
            score = sum(tmp)-self_
            n_ = n-1
        elif self_==min_ and tmp.count(self_) == 1:
            score = sum(tmp)-self_
            n_ = n-1
        else:
            score = sum(tmp)
            n_ = n
            
        score = score/n_
        if score >= 90:
            answer += 'A'
        elif score >= 80:
            answer += 'B'
        elif score >= 70:
            answer += 'C'
        elif score >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer