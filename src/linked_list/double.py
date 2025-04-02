class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, data: int):
        node = DoubleNode(data)
        if not self.head:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_end(self, data: int):
        node = DoubleNode(data)
        if not self.head:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def delete_start(self):
        if self.head:
            if self.head.next:
                self.head.prev = None
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None

    def delete_end(self):
        if self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None

    def delete_any(self, key: int):
        start = self.head
        end = self.tail

        if start is None:
            return

        if start and start.data == key:
            self.head = start.next
            if start.next:
                start.next.prev = None
            return

        if end and end.data == key:
            self.tail = end.prev
            end.prev.next = None
            return

        while start:
            if start.data == key:
                if start.next:
                    start.next.prev = start.prev
                if start.prev:
                    start.prev.next = start.next
            start = start.next

    def search(self, key: int) -> bool:
        start = self.head
        while start:
            if start.data == key:
                print("Element is found")
                return True
            start = start.next
        print("Element not found")
        return False

    def reverse(self):
        curr = self.head
        prev = None
        self.head = self.tail

        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        
        self.head = prev

    def print_start(self):
        start = self.head
        while start:
            print(start.data, end="" if start.next else "\n")
            start = start.next

    def print_end(self):
        start = self.tail
        while start:
            print(start.data, end="" if start.prev else "\n")
            start = start.prev


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
