from collections import deque

#FIFO#
class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)
        return self.buffer
        
    def dequeue(self):
        return self.buffer.pop()
        
    def is_empty(self):
        return len(self.buffer) == 0
        
    def size(self):
        return len(self.buffer)
        
        
d = Queue()
print(d.enqueue({"name":"mayowa"}))
print(d.enqueue({"name":"tosin"}))
print(d.enqueue({"name":"wale"}))
print(d.dequeue())
print(d.buffer)