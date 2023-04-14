from trees import AVLTree
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# Create a new AVL tree
tree = AVLTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Print the tree
tree.print_bf()
