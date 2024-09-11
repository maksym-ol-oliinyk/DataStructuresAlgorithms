from collections import deque

#as array
listQueue = []
listQueue.insert(0, "elem1")
listQueue.insert(0, "elem2")
listQueue.insert(0, "elem3")
print(listQueue.pop())

#with deque
class Queue:
    def __init__(self):
        self.collection = deque()
    
    def enqueue(self, val):
        self.collection.appendleft(val)

    def dequeue(self):
        return self.collection.pop()
    
    def size(self):
        return len(self.collection)

    def isEmpty(self):
        return self.size() == 0
    
queue = Queue()
queue.enqueue("elem1")
queue.enqueue("elem2")
queue.enqueue("elem3")
print(queue.dequeue())


