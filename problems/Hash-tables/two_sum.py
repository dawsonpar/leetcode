"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Solution
- Create a hashmap
- Iterate through the array
    - If we see the counterpart in our hashmap then return the index of the counterpart and current index
    - Store the counterpart of the number we have seen and current index
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hashmap
        hashmap = dict()

        # Iterate through the array
        for i, num in enumerate(nums):
            # If we see the counterpart in our hashmap then return the index of the counterpart and current index
            if num in hashmap:
                return [hashmap[num], i]

            # Store the counterpart of the number we have seen and current index
            hashmap[target - num] = i
