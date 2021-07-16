a = [1, 2, 2, 3]
b = {1:2, 2:3, 3:5, 4:5}

q = [(a, b)]
for _ in range(2):
    x, y = q.pop()
    x.append()