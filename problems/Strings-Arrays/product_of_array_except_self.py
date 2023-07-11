"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Solution
Initialize each position in result to be 1
Do one pass through the array and update the output array by multiplying the current position by nums[i]
Do another pass from the end of the nums array and multiply the current position of the output by nums[i]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nuns) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
