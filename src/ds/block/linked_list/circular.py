class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        node = CircularNode(data)
        if not self.head:
            self.head = node
            node.next = node
            return

        node.next = self.head
        last = self.head

        while last.next != self.head:
            last = last.next

        last.next = node
        self.head = node

    def insert_end(self, data):
        node = CircularNode(data)
        if not self.head:
            self.head = node
            node.next = node
            return

        node.next = self.head
        last = self.head

        while last.next != self.head:
            last = last.next

        last.next = node

    def delete_start(self):
        if not self.head:
            return

        if self.head.next is self.head:
            self.head = None
            return

        self.head.data = self.head.next.data
        self.head.next = self.head.next.next

    def delete_end(self):
        if not self.head:
            return

        if self.head.next is self.head:
            self.head = None
            return

        last = self.head
        while last.next.next != self.head:
            last = last.next

        last.next = self.head

    def search(self, key):
        start = self.head
        while start:
            if start.data == key:
                return True
            if start.next == self.head:
                return False
            start = start.next
        return False

    def print_items(self):
        start = self.head
        while start:
            print(start.data, end="")
            start = start.next
            if start is self.head:
                break

    def reverse(self):
        if not self.head or self.head.next is self.head:
            return

        prev = self.head
        next = self.head
        curr = self.head.next

        prev.next = prev

        while curr != self.head:
            next = curr.next
            curr.next = prev
            self.head.next = curr
            prev = curr
            curr = next

        self.head = prev


class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None
