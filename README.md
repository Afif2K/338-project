# 338-project
# libds - Data Structures Library

`libds` is a Python library that provides various data structures and algorithms for working with them. It includes implementations of linked lists, stacks, queues, trees, heaps, and graph algorithms.

## Installation

To install the `libds` library from PyPI, run the following command:

```bash
pip install libds
```
Alternatively, you can clone the GitHub repository and install the package locally:
git clone https://github.com/Afif2K/338-project.git
```
cd libds
pip install -e .
```
## Usage
Here is an example of how to use the libds library:
```
from libds.datastructures import SinglyLinkedList, SNode

sll = SinglyLinkedList()
sll.insert_head(SNode(3))
sll.insert_tail(SNode(5))
sll.insert(SNode(4), 2)
sll.print()
```
## Data Structures and Algorithms
The following data structures and algorithms are included in the library:

Singly Linked List
Doubly Linked List
Circular Singly Linked List
Circular Doubly Linked List
Stack
Queue
Binary Search Tree
AVL Tree
Min Heap
Max Heap
Graph Algorithms
Breadth-First Search (BFS)
Depth-First Search (DFS)
Dijkstra's Shortest Path Algorithm
