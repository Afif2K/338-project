from datastructures.trees import AVLTree, BinarySearchTree
from datastructures.nodes import SNode, DNode
from datastructures.heap import MaxH, MinH
from datastructures.linear import SinglyLinkedList, DoublyLinkedList, CircularDoublyLinkedList, CircularSinglyLinkedList, Stack, Queue


def main():
    # Test SinglyLinkedList
    print("Testing SinglyLinkedList:")
    sll = SinglyLinkedList()
    sll.insert_head(SNode(3))
    sll.insert_tail(SNode(5))
    sll.insert(SNode(4), 2)
    sll.print()
    print("Test Count: 1")

    # Test DoublyLinkedList
    print("\nTesting DoublyLinkedList:")
    dll = DoublyLinkedList()
    dll.insert_head(DNode(3))
    dll.insert_tail(DNode(5))
    dll.insert(DNode(4), 2)
    dll.print()
    print("Test Count: 2")

    # Test CircularSinglyLinkedList
    print("\nTesting CircularSinglyLinkedList:")
    csll = CircularSinglyLinkedList()
    csll.insert_head(SNode(3))
    csll.insert_tail(SNode(5))
    csll.insert(SNode(4), 2)
    csll.print()
    print("Test Count: 3")

    # Test CircularDoublyLinkedList
    print("\nTesting CircularDoublyLinkedList:")
    cdll = CircularDoublyLinkedList()
    cdll.insert_head(DNode(3))
    cdll.insert_tail(DNode(5))
    cdll.insert(DNode(4), 2)
    cdll.print()
    print("Test Count: 4")

    # Test Stack
    print("\nTesting Stack:")
    stack = Stack()
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    stack.print()
    print("Test Count: 5")

    # Test Queue
    print("\nTesting Queue:")
    queue = Queue()
    queue.enqueue(SNode(1))
    queue.enqueue(SNode(2))
    queue.enqueue(SNode(3))
    queue.print()
    print("Test Count: 6")

    # Test Binary Search Tree
    print("\nTesting Binary Search Tree:")
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(5)
    bst.insert(4)
    bst.print()
    print("Test Count: 7")

    # Test AVL Tree
    print("\nTesting AVL Tree:")
    avl = AVLTree()
    avl.insert(3)
    avl.insert(5)
    avl.insert(4)
    avl.print()
    print("Test Count: 8")

    # Test Min Heap and Max Heap
    print("\nTesting Min Heap and Max Heap:")
    min_heap = MinH()
    max_heap = MaxH()
    data = [4, 1, 7, 3, 8, 5]
    for val in data:
        min_heap.insert(val)
        max_heap.insert(val)

    print("Min Heap:")
    while not min_heap.isEmpty():
        print(min_heap.delete(), end=" ")
    print("\nMax Heap:")
    while not max_heap.isEmpty():
        print(max_heap.delete(), end=" ")
    print("\nTest Count: 9")

    # Test heap sort
    print("\n\nTesting heap sort:")
    unsorted_arr = [8, 3, 6, 1, 9, 4]
    heap = MinH(unsorted_arr)
    sorted_arr = heap.sort()
    print(f"Unsorted array:{unsorted_arr}")
    print(f"Sorted array: {sorted_arr}")
    print("Test Count: 10")


if __name__ == "__main__":
    main()
