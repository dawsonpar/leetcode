"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.

Solution
- Create a max heap and remove k elements from heap
- Return the kth largest element which should be at the top of the heap
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapify the array with negative values
        heap = [-num for num in nums]
        heapq.heapify(heap)

        # remove k items from heap
        for _ in range(1, k):
            heapq.heappop(heap)

        # return the top of the heap
        return neg(heap[0])
