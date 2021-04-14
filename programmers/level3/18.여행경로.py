tickets =  [['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]


import heapq
answer = None

def search(start, tickets, used, path):
    global answer
    if all(used):
        if answer is None:
            answer = path
        return

    if start not in tickets.keys():
        return 

    for to, i in tickets[start]:
        if not used[i]:
            used[i] = True
            search(to, tickets, used, path+[to])
            used[i] = False


def solution(tickets):
    global answer
    answer = None
    ticket_dct = {}
    for i, (f, t) in enumerate(tickets):
        if f not in ticket_dct.keys():
            ticket_dct[f] = []
        heapq.heappush(ticket_dct[f], (t, i))
        
    for k in ticket_dct.keys():
        ticket_dct[k].sort()
        
    used = [False] * (i+1)
    search('ICN', ticket_dct, used, ['ICN'])
    return answer

answer = None
solution(tickets)