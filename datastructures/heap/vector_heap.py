import heapq


class Heap:
    def __init__(self, arr=None):
        self.elements = []
        if arr is not None:
            self.heapify(arr)

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def clear(self):
        self.elements = []

    def contains(self, value):
        return value in self.elements

    def insert(self, key):
        heapq.heappush(self.elements, key)

    def delete(self, key):
        try:
            idx = self.elements.index(key)
            removed_element = self.elements.pop(idx)
            heapq.heapify(self.elements)
            return removed_element
        except ValueError:
            return None

    def sort(self):
        return heapq.nsmallest(len(self.elements), self.elements)

    def print(self):
        print(self.elements)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, x, y):
        self.elements[x], self.elements[y] = self.elements[y], self.elements[x]

    def heapify(self, arr):
        heapq.heapify(arr)
        self.elements = arr


class MinH(Heap):
    def __init__(self, arr=None):
        super().__init__(arr)


class MaxH(Heap):
    def __init__(self, arr=None):
        if arr is not None:
            arr = [-x for x in arr]
        super().__init__(arr)

    def insert(self, key):
        heapq.heappush(self.elements, -key)

    def delete(self, key):
        try:
            idx = self.elements.index(-key)
            removed_element = self.elements.pop(idx)
            heapq.heapify(self.elements)
            return -removed_element
        except ValueError:
            return None

    def pop(self):
        if not self.is_empty():
            return -heapq.heappop(self.elements)
        return None

    def sort(self):
        return [-x for x in heapq.nsmallest(len(self.elements), self.elements)]
