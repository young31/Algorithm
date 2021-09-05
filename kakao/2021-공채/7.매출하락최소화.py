from collections import defaultdict

def solution(sales, links):
    sales = [0] + sales
    graph = defaultdict(list)
    for a, b in links:
        graph[a].append(b)

    print(graph)
    def search(x):
        if not graph[x]:
            return (sales[x], 0)
        else:
            cur = sales[x]
            child_sales = []
            for child in graph[x]:
                child_sales.append(search(child))
            own = cur + sum([min(cs) for cs in child_sales])
            child_min = []
            for i in range(len(child_sales)):
                child_min.append(child_sales[i][0] + sum([min(cs) for j, cs in enumerate(child_sales) if j != i]))
            return (own, min(child_min))

    answer = min(search(1))
    return answer

sales = [10, 10, 1, 1]
links = [[3,2], [4,3], [1,4]]
solution(sales, links)