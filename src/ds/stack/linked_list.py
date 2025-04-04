class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        self.size += 1

    def pop(self):
        if not self.head:
            return
        elif not self.head.next:
            self.head = None
            return

        last = self.head
        while last.next and last.next.next:
            last = last.next
        last.next = None
        self.size -= 1

    def peek(self):
        last = self.head
        while last.next:
            last = last.next
        return last.data

    def isEmpty(self):
        return True if self.head else False

    def stackSize(self):
        return self.size


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
