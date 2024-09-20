from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        use a decision tree and backtracking
        one decision includes the current element trying to reach the target
        the other decision excludes the current element

        base cases
        target is reached
        pointer is out of bounds
        total > target

        O(2^t) where t is the target
        """
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res
