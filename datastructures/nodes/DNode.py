class DNode(SNode):
    def __init__(self, data=None, next_node=None, prev_node=None):
        super().__init__(data, next_node)
        self.prev = prev_node

    # Setters
    def set_prev(self, prev_node):
        self.prev = prev_node

    # Getters
    def get_prev(self):
        return self.prev

    # Print and String representation
    def print_node(self):
        print(f"DNode: Data={self.data}")

    def __str__(self):
        return str(self.data)
