class SNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    # Setters
    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next = next_node

    # Getters
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    # Print and String representation
    def print_node(self):
        print(f"SNode: Data={self.data}")

    def __str__(self):
        return str(self.data)
