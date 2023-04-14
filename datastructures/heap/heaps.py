import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0


class HeapUtils:
    @staticmethod
    def heapsort(arr):
        min_heap = MinHeap()
        for val in arr:
            min_heap.push(val)
        sorted_arr = []
        while not min_heap.is_empty():
            sorted_arr.append(min_heap.pop())
        return sorted_arr
