import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        if self.size() == 0:
            print(-1)
        else:
            a = self.s.pop()
            print(a)

    def size(self, out=False):
        l = len(self.s)
        if out:
            print(l)
        return l

    def empty(self):
        if self.size() == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if self.size() == 0:
            print(-1)
        else:
            print(self.s[-1])

n = int(input())
stack = Stack()
for _ in range(n):
    s = input().split()
    if s[0] == 'push':
        stack.push(s[1])
    elif s[0] == 'pop':
        stack.pop()
    elif s[0] == 'size':
        stack.size(out=True)
    elif s[0] == 'empty':
        stack.empty()
    elif s[0] == 'top':
        stack.top()
        