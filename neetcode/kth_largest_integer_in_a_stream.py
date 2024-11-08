"""
Heaps and priority queues in Python: https://realpython.com/python-heapq-module/

For an element at index k:

The first child is at 2k + 1
The second child is at 2k + 2
The parent is at (k - 1)//2

Pushing and popping from a heap is a log(n) time complexity operation

Sample code:
import heapq
a = [3, 5, 1, 2, 6, 8, 7]
heapq.heapify(a)
heapq.heappop(a)
heapq.heappush(a, 4)


merge takes k sorted iterables of TOTAL length n and merges them log(k)*n, space is O(k)
heapify has time complexity O(n)
"""
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]