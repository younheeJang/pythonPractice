class Queue:
    def __init__(self):
        self.queue = list()
    def add(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        return False
    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in queue")
    def size(self):
        return len(self.queue)
    def printQueue(self):
        if len(self.queue) > 0:
            print(self.queue)


aQueue = Queue()
aQueue.add("curious")
aQueue.add("jeager")
aQueue.add("queue")
print(aQueue.size())
aQueue.printQueue()
aQueue.remove()
aQueue.printQueue()