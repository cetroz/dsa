class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        node = SingleNode(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        node = SingleNode(data)
        if not self.head:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def delete_start(self):
        if not self.head:
            return
        self.head = self.head.next

    def delete_end(self):
        if not self.head:
            return
        elif not self.head.next:
            self.head = None
            return

        last = self.head
        while last.next and last.next.next:
            last = last.next
        last.next = None

    def delete_any(self, key):
        start = self.head
        prev = None

        if start and start.data == key:
            self.head = start.next
            return

        while start and start.data != key:
            prev = start
            start = start.next

        if not start:
            return

        prev.next = start.next

    def reverse(self):
        if not self.head:
            return

        if self.head.next is None:
            return

        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def search(self, key):
        start = self.head
        while start:
            if start.data == key:
                return True
            start = start.next
        return False

    def print_items(self):
        start = self.head
        while start:
            print(start.data, end="" if start.next else "\n")
            start = start.next


class SingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
