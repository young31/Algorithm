routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
routes = [[2, 3], [3, 4], [4, 6], [6, 8]]
routes = [[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]


def solution(routes):
    answer = 0
    r_sort = sorted(routes, key=lambda x: x[1])
    routes = sorted(routes, key=lambda x: x[0])

    l = r = 0
    done = []
    while (l < len(routes)):
        if r_sort[r] not in done:
            start = r_sort[r][1]
            r += 1
            answer += 1
        else:
            r += 1
            continue

        c = 0
        for route in routes[l:]:
            if route[0] <= start <= route[1]:
                done.append(route)
                c += 1
            else:
                break
        l += c

    print(answer)
    return answer

solution(routes)
print(-14 <= -13 <= -5)