"""Make a Queue class using a list!
"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]
    
    # enqueue: append new element at the end
    def enqueue(self, new_element):
        self.storage.append(new_element)
    
    # return first item in the queue
    def peek(self):
        return self.storage[0]

    # pop out the first item in the queue
    # pop() return the popped item.
    def dequeue(self):
        return self.storage.pop(0)
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()