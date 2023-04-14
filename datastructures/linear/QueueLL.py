class Queue(SinglyLinkedList):
    def __init__(self, head=None):
        super().__init__(head)

    def enqueue(self, node):
        super().insert_tail(node)

    def dequeue(self):
        if self.head is None:
            raise IndexError("Queue is empty")
        dequeued_node = self.head
        super().delete_head()
        return dequeued_node

    def peek(self):
        if self.head is None:
            raise IndexError("Queue is empty")
        return self.head

    def is_empty(self):
        return self.head is None

    # Override methods that do not apply to queues with empty bodies
    def insert_head(self, node):
        pass

    def insert(self, node, position):
        pass

    def sorted_insert(self, node):
        pass

    def search(self, node):
        pass

    def delete_head(self):
        pass

    def delete_tail(self):
        pass

    def delete(self, node):
        pass

    def sort(self):
        pass

    def clear(self):
        super().clear()

    def print(self):
        super().print()
