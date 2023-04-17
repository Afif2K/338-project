from libds.datastructures.linear.DLL import DoublyLinkedList


class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self, head=None):
        super().__init__(head)
        if head:
            self.tail = head
            head.prev = head
            head.next = head

    def insert_head(self, node):
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        self.tail.next = self.head
        self.head.prev = self.tail
        self.size += 1

    def insert_tail(self, node):
        super().insert_tail(node)
        self.tail.next = self.head
        self.head.prev = self.tail

    def insert(self, node, position):
        super().insert(node, position)
        if position == 1:
            self.tail.next = self.head
            self.head.prev = self.tail

    def delete_head(self):
        super().delete_head()
        if self.tail is not None:
            self.tail.next = self.head
            self.head.prev = self.tail

    def delete_tail(self):
        super().delete_tail()
        if self.head is not None:
            self.tail.next = self.head
            self.head.prev = self.tail

    def print(self):
        print(f"List length: {self.size}")
        print(f"Sorted status: {'Yes' if self.is_sorted() else 'No'}")
        print("List content:")
        if self.head:
            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
        print("None")
