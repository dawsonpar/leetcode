"""
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
    KthLargest(int k, int[] nums): Initializes the object with the integer k and the stream of integers nums.
    int add(int val): Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Solution
- Create a min-heap and limit it's size to k. The first element will be the kth largest element
- Remove k + 1 largest val from heap
"""


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(minHeap)
        return self.minHeap[0]
