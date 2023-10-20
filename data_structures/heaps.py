"""Heap is a special tree structure in which each parent node is less than or equal to its child node. Then it is
called a Min Heap. If each parent node is greater than or equal to its child node then it is called a max heap. It is
very useful is implementing priority queues where the queue item with higher weightage is given more priority in
processing."""

import heapq

class MinMaxHeap:
    def __init__(self):
        """
        Initialize an empty min-max heap.
        """
        self.min_heap = []
        self.max_heap = []

    def insert(self, value):
        """
        Insert a value into both the min-heap and max-heap.

        :param value: The value to be inserted.
        """
        heapq.heappush(self.min_heap, value)
        heapq.heappush(self.max_heap, -value)

    def extract_min(self):
        """
        Extract and return the minimum value from the min-heap.

        :return: The minimum value.
        """
        if not self.min_heap:
            raise IndexError("Min-Heap is empty.")
        return heapq.heappop(self.min_heap)

    def extract_max(self):
        """
        Extract and return the maximum value from the max-heap.

        :return: The maximum value.
        """
        if not self.max_heap:
            raise IndexError("Max-Heap is empty.")
        return -heapq.heappop(self.max_heap)

    def get_min(self):
        """
        Get the minimum value from the min-heap without removing it.

        :return: The minimum value.
        """
        if not self.min_heap:
            raise IndexError("Min-Heap is empty.")
        return self.min_heap[0]

    def get_max(self):
        """
        Get the maximum value from the max-heap without removing it.

        :return: The maximum value.
        """
        if not self.max_heap:
            raise IndexError("Max-Heap is empty.")
        return -self.max_heap[0]

    def size_min(self):
        """
        Get the number of elements in the min-heap.

        :return: The number of elements in the min-heap.
        """
        return len(self.min_heap)

    def size_max(self):
        """
        Get the number of elements in the max-heap.

        :return: The number of elements in the max-heap.
        """
        return len(self.max_heap)

    def is_empty_min(self):
        """
        Check if the min-heap is empty.

        :return: True if the min-heap is empty, otherwise False.
        """
        return len(self.min_heap) == 0

    def is_empty_max(self):
        """
        Check if the max-heap is empty.

        :return: True if the max-heap is empty, otherwise False.
        """
        return len(self.max_heap) == 0

# Example usage:
min_max_heap = MinMaxHeap()
min_max_heap.insert(5)
min_max_heap.insert(3)
min_max_heap.insert(8)
min_max_heap.insert(1)

print("Min-Heap:")
while not min_max_heap.is_empty_min():
    print(min_max_heap.extract_min())

print("Max-Heap:")
while not min_max_heap.is_empty_max():
    print(min_max_heap.extract_max())
