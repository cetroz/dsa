class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return
        self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
