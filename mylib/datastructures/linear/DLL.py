from mylib.datastructures.linear.SLL import Node
from mylib.datastructures.linear.SLL import SinglyLinkedList


class DNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self, head=None):
        super().__init__(head)
        if head:
            self.tail = head
            head.prev = None
            head.next = None

    def insert_head(self, node):
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def insert_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def insert(self, node, position):
        if position <= 0 or position > self.size + 1:
            raise IndexError("Invalid position")
        elif position == 1:
            self.insert_head(node)
        elif position == self.size + 1:
            self.insert_tail(node)
        else:
            current = self.head
            for _ in range(position - 2):
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.size += 1

    def delete_head(self):
        if self.head is not None:
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next
            self.size -= 1

    def delete_tail(self):
        if self.tail is not None:
            if self.tail.prev is not None:
                self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size -= 1

    def delete(self, node):
        if self.head == node:
            self.delete_head()
        elif self.tail == node:
            self.delete_tail()
        else:
            current = self.head
            while current.next and current.next != node:
                current = current.next
            if current.next:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                self.size -= 1
