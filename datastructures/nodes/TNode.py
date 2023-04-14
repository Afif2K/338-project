class TNode:
    def __init__(self, data=None, balance=0, parent=None, left=None, right=None):
        self.data = data
        self.balance = balance
        self.parent = parent
        self.left = left
        self.right = right

    # Setters
    def set_data(self, data):
        self.data = data

    def set_balance(self, balance):
        self.balance = balance

    def set_parent(self, parent):
        self.parent = parent

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    # Getters
    def get_data(self):
        return self.data

    def get_balance(self):
        return self.balance

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    # Print node information
    def print(self):
        print(f"Node Data: {self.data}, Balance: {self.balance}")

    # Convert node data to string
    def __str__(self):
        return str(self.data)

    # Constructors
    @classmethod
    def default_constructor(cls):
        return cls()

    @classmethod
    def overload_constructor(cls, data, balance, parent, left, right):
        return cls(data, balance, parent, left, right)
