from .BST import BinarySearchTree
from libds.datastructures.nodes.TNode import TNode


class AVLTree(BinarySearchTree):
    def __init__(self, root=None):
        super().__init__(root)

    # Constructors
    @classmethod
    def default_constructor(cls):
        return cls()

    @classmethod
    def overload_constructor_with_val(cls, val):
        return cls(TNode(data=val, balance=0))

    @classmethod
    def overload_constructor_with_node(cls, node):
        tree = cls(node)
        tree._create_balanced_tree(tree.root)
        return tree

    # Setter and getter for root
    def set_root(self, root):
        if root is not None and (root.left is not None or root.right is not None):
            self._create_balanced_tree(root)
        self.root = root

    def get_root(self):
        return self.root

    # Insert methods
    def insert(self, val):
        new_node = TNode(data=val, balance=0)
        self.root = self._insert_node(self.root, new_node)
        self.root = self._balance_tree(self.root)

    def insert_node(self, node):
        self.root = self._insert_node(self.root, node)
        self.root = self._balance_tree(self.root)

    # Bonus: Delete method
    def delete(self, val):
        self.root = self._delete_node(self.root, val)
        self.root = self._balance_tree(self.root)

    # Helper functions
    def _create_balanced_tree(self, node):
        if node is not None:
            self._create_balanced_tree(node.left)
            self.insert_node(node)
            self._create_balanced_tree(node.right)

    def _update_balance(self, node):
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1
        node.balance = right_height - left_height

    def _balance_tree(self, node):
        if node is None:
            return node

        self._update_balance(node)

        if node.balance > 1:
            if node.right.balance < 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        elif node.balance < -1:
            if node.left.balance > 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)

        return node

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self._update_balance(node)
        self._update_balance(new_root)

        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self._update_balance(node)
        self._update_balance(new_root)

        return new_root
