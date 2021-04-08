jobs = [[0, 3], [1, 9], [2, 6]]

import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    time = 0
    working = []
    done = []
    cnt = 0
    while cnt < n:
        # print(jobs, working)
        for job in jobs:
            if job[0] <= time and job not in done:
                heapq.heappush(working, (job[1], job[0]))
                done.append(job)

        if len(working) == 0:
            time += 1
            continue
        dur, start = heapq.heappop(working)
        cnt += 1

        time += dur
        answer += time-start

        # print(answer, time)
    answer = int(answer/n)
    print(answer)
    return answer

solution(jobs)