class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0 if head is None else 1

    def insert_head(self, node):
        node.next = self.head
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
            current.next = node
            self.size += 1

    def is_sorted(self):
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sorted_insert(self, node):
        if not self.is_sorted():
            self.sort()
        if self.head is None or node.data <= self.head.data:
            self.insert_head(node)
        else:
            current = self.head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
            if node.next is None:
                self.tail = node
            self.size += 1

    def search(self, node):
        current = self.head
        while current:
            if current == node:
                return current
            current = current.next
        return None

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next
            self.size -= 1

    def delete_tail(self):
        if self.tail is not None:
            current = self.head
            while current.next and current.next != self.tail:
                current = current.next
            if current.next:
                current.next = None
                self.tail = current
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
                self.size -= 1

    def sort(self):
        if self.head:
            sorted_list = SinglyLinkedList()
            current = self.head
            while current:
                next_node = current.next
                current.next = None
                sorted_list.sorted_insert(current)
                current = next_node
            self.head = sorted_list.head
            self.tail = sorted_list.tail

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print(self):
        print(f"List length: {self.size}")
        print(f"Sorted status: {'Yes' if self.is_sorted() else 'No'}")
        print("List content:")
        current = self.head
       
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
