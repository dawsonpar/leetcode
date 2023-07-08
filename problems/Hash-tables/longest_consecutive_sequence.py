"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Solution
- Create a hashset
- Loop through the hashset
- If the current number has no left neighbor then start streak
- While the set contains currentNum + 1, increment currentNum and currentStreak
- After each while loop, check and set longestStreak
- Return longestStreak
"""


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        # Sort the array
        nums.sort()

        # Keep track of current length count (current) and longest length count (longest). Both starting at 1.
        longest_streak = 1
        current_streak = 1

        # Loop through the sorted array
        for i in range(1, len(nums)):
            # skip duplicates
            if nums[i] == nums[i - 1]:
                continue

            # If current number is one more than previous number add to current streak
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            # Else set longest streak and reset current streak
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        # Return the longest streak
        return max(longest_streak, current_streak)
