"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Solution
Store the elements in a set and check if the element already exists in the set.
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create Set
        hashSet = set()

        # Iterate through numbers
        for num in nums:
            # If number is already in set return True
            if num in hashSet:
                return True

            # Store number in set
            hashSet.add(num)

        # Return False (we have reached the end of the list without duplicate)
        return False
