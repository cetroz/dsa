class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None

        self.head = self.head.next
        self.size -= 1

    def peek(self):
        if not self.tail:
            return
        return self.tail.data

    def isEmpty(self):
        return False if self.head else True

    def queueSize(self):
        return self.size


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
