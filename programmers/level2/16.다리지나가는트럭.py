bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]
# truck_weights = [10,10,10,10,10,10,10,10,10,10]

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    n = len(truck_weights)
    bridge = deque([0]*bridge_length, maxlen=bridge_length)

    arrived = 0
    cur = truck_weights.pop(0)
    S = 0
    while arrived < n:
        k = weight-(S - bridge[0])
        if cur <= k and cur != 0:
            if bridge[0] != 0:
                arrived += 1
            S += cur-bridge[0]
            bridge.append(cur)
            
            if truck_weights:
                cur = truck_weights.pop(0)
            else:
                cur = 0
        else:
            if bridge[0] != 0:
                S -= bridge[0]
                arrived += 1
            bridge.append(0)

        answer += 1
        print(bridge)
    print(answer)
    return answer



solution(bridge_length, weight, truck_weights)