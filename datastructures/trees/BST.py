from datastructures.nodes.TNode import TNode


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    # Constructors
    @classmethod
    def default_constructor(cls):
        return cls()

    @classmethod
    def overload_constructor_with_val(cls, val):
        return cls(TNode(data=val))

    @classmethod
    def overload_constructor_with_node(cls, node):
        return cls(root=node)

    # Setter and getter for root
    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    # Helper method to insert a node recursively
    def _insert_node(self, current, node):
        if current is None:
            return node
        if node.data < current.data:
            current.left = self._insert_node(current.left, node)
        else:
            current.right = self._insert_node(current.right, node)
        return current

    # Insert methods
    def insert(self, val):
        new_node = TNode(data=val)
        self.root = self._insert_node(self.root, new_node)

    def insert_node(self, node):
        self.root = self._insert_node(self.root, node)

    # Delete method
    def delete(self, val):
        self.root = self._delete_node(self.root, val)

    # Helper method to find the minimum value node
    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Helper method to delete a node with the given key
    def _delete_node(self, root, key):
        if root is None:
            print("Value not found in the tree.")
            return root

        if key < root.data:
            root.left = self._delete_node(root.left, key)
        elif key > root.data:
            root.right = self._delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self._find_min_node(root.right).data
            root.right = self._delete_node(root.right, root.data)
        return root

    # Search method
    def search(self, val):
        return self._search_node(self.root, val)

    # Helper method to search a node recursively
    def _search_node(self, current, val):
        if current is None or current.data == val:
            return current
        if val < current.data:
            return self._search_node(current.left, val)
        return self._search_node(current.right, val)

    # Print in-order
    def print_in_order(self):
        self._in_order(self.root)
        print()

    # Helper method to print in-order
    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.data, end=" ")
            self._in_order(node.right)

    # Print Breadth-First
    def print_bf(self):
        if self.root is None:
            print("Tree is empty.")
            return

        queue = [self.root]
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                print(node.data, end=" ")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()
