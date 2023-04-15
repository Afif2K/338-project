from mylib.datastructures.linear.SLL import SinglyLinkedList


class CircularSinglyLinkedList(SinglyLinkedList):
    def __init__(self, head=None):
        super().__init__(head)
        if head:
            self.tail = head
            head.next = head

    def insert_head(self, node):
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.tail.next = self.head
        self.size += 1

    def insert_tail(self, node):
        super().insert_tail(node)
        self.tail.next = self.head

    def insert(self, node, position):
        super().insert(node, position)
        if position == 1:
            self.tail.next = self.head

    def delete_head(self):
        super().delete_head()
        if self.tail is not None:
            self.tail.next = self.head

    def delete_tail(self):
        if self.tail is not None:
            current = self.head
            while current.next and current.next != self.tail:
                current = current.next
            if current.next:
                current.next = self.head
                self.tail = current
                self.size -= 1

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
