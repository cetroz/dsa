class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, data):
        node = CircularDoubleNode(data)
        if not self.head:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node
            return
        
        self.tail.next = node
        node.prev = self.tail

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_end(self, data):
        node = CircularDoubleNode(data)
        if not self.head:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node
            return
        
        self.tail.next = node
        node.prev = self.tail
        node.next = self.head
        self.head.prev = node
        self.tail = node

    def delete_start(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail.next = self.head.next
            self.head = self.head.next
            self.head.prev = self.tail

    def delete_end(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            last = self.tail.prev
            self.tail = last
            last.next = self.head
            self.head.prev = last

    def delete_any(self, key):
        start = self.head
        end = self.tail

        if start is None:
            return
        
        if start == end:
            self.head = self.tail = None

        if start and start.data == key:
            self.head = start.next
            start.next.prev = self.tail
            self.tail.next = self.head

        if end and end.data == key:
            self.tail = end.prev
            self.tail.next = self.head
            self.head.prev = self.tail

        while start.next != self.head:
            if start.data == key:
                if start.next:
                    start.next.prev = start.prev
                if start.prev:
                    start.prev.next = start.next
            start = start.next

    def search(self, key):
        start = self.head
        
        if not self.head:
            return False
        
        if self.head.data == key:
            return True
        
        if self.tail.data == key:
            return True
        
        while start.next != self.head:
            if start.data == key:
                return True
            start = start.next
        return False

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

    def print_items(self):
        start = self.head
        while start:
            print(start.data, end='')
            start = start.next
            if start is self.head:
                break


class CircularDoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

if __name__ == "__main__":
    llist = CircularDoubleLinkedList()
    llist.insert_end(4)
    llist.insert_end(3)
    llist.insert_end(2)
    llist.reverse()
    llist.print_items()