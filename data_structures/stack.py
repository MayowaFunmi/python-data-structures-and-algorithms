# stacks in python
from collections import deque
stack = deque()
print(dir(stack))   # available methods
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')
stack.append('f')
#print(stack)
print()

# create a stack object
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def list(self):
        return self.container

s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.push('d')
s.push('e')
s.push('f')
print(s.list())

print()

# reverse string
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))
