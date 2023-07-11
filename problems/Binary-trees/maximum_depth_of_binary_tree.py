"""
Given a binary tree find the maximum depth

Solution
Recursive DFS
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Basecase is a Null Node, return 0
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
