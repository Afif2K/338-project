from datastructures import *


def test_graph_algorithms():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    print("\nTesting BFS:")
    bfs_result = GraphAlgo.bfs(graph, 'A')
    print("BFS visited nodes:", bfs_result)

    print("\nTesting DFS:")
    dfs_result = GraphAlgo.dfs(graph, 'A')
    print("DFS visited nodes:", dfs_result)

    print("\nTesting Dijkstra's Algorithm:")
    shortest_path = GraphAlgo.dijkstra(graph, 'A', 'D')
    print("Shortest path from A to D:", shortest_path)


def main():
    # Test SinglyLinkedList
    print("Testing SinglyLinkedList:")
    sll = SinglyLinkedList()
    sll.insert_head(SNode(3))
    sll.insert_tail(SNode(5))
    sll.insert(SNode(4), 2)
    sll.print()

    # Test DoublyLinkedList
    print("\nTesting DoublyLinkedList:")
    dll = DoublyLinkedList()
    dll.insert_head(DNode(3))
    dll.insert_tail(DNode(5))
    dll.insert(DNode(4), 2)
    dll.print()

    # Test CircularSinglyLinkedList *PROBLEM*
    print("\nTesting CircularSinglyLinkedList:")
    csll = CircularSinglyLinkedList()
    csll.insert_head(SNode(3))
    csll.insert_tail(SNode(5))
    csll.insert(SNode(4), 2)
    csll.print()

    # Test CircularDoublyLinkedList *PROBLEM*
    print("\nTesting CircularDoublyLinkedList:")
    cdll = CircularDoublyLinkedList()
    cdll.insert_head(DNode(3))
    cdll.insert_tail(DNode(5))
    cdll.insert(DNode(4), 2)
    cdll.print()

    # Test Stack
    print("\nTesting Stack:")
    stack = Stack()
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    stack.print()

    # Test Queue
    print("\nTesting Queue:")
    queue = Queue()
    queue.enqueue(SNode(1))
    queue.enqueue(SNode(2))
    queue.enqueue(SNode(3))
    queue.print()

    # Test Binary Search Tree
    print("\nTesting Binary Search Tree:")
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(5)
    bst.insert(4)
    bst.print_in_order()

    # Test AVL Tree
    print("\nTesting AVL Tree:")
    avl = AVLTree()
    avl.insert(3)
    avl.insert(5)
    avl.insert(4)
    avl.print_bf()

    # Test Min Heap and Max Heap
    print("\nTesting Min Heap and Max Heap:")
    min_heap = MinH()
    max_heap = MaxH()
    data = [4, 1, 7, 3, 8, 5]
    for val in data:
        min_heap.insert(val)
        max_heap.insert(val)

    print("Min Heap:")
    while not min_heap.is_empty():
        value = min_heap.delete(min_heap.elements[0])
        if value is not None:
            print(value, end=" ")

    print("\nMax Heap:")
    value = max_heap.pop()
    while value is not None:
        print(value, end=" ")
        value = max_heap.pop()

    # Add this line at the end of the main function
    test_graph_algorithms()


if __name__ == "__main__":
    main()
