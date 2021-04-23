files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat", "A- 10 Thunderbolt II", "abc123defg123.jpg"]

def split(x):
    head = ''
    number = ''
    tail = ''
    flag = False

    i = 0
    while i < len(x):
        # print(i)
        if not flag:
            try:
                int(x[i])
                head = x[:i]
                flag = True
                j = i
                i += 1
            except:
                if x[i] == '-':
                    ''
                i += 1

        else:
            try:
                int(x[i])
                i += 1
            except:
                number = x[j:i]
                break
    if number == '':
        number = x[j:]
    print(head, number)
    return (head.lower(), int(number))


def solution(files):
    answer = sorted(files, key=lambda x: split(x))
    print(answer)
    return answer

# solution(files)

print(split('F-15'))