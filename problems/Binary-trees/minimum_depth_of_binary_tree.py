""" 
Given a binary tree find the minimum depth


Solution
Recursive DFS
If both children check min between depths
If single child check depth of child
If leaf return it's height
"""


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Basecase is a Null Node, return 0
        if not root:
            return 0

        # Recursively check the minimum height from a node
        if root.left and root.right:
            # If both children check min between depths
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.right:
            # If single child check depth of child
            return self.minDepth(root.right) + 1
        elif root.left:
            # If single child check depth of child
            return self.minDepth(root.left) + 1
        else:
            # If leaf return it's height.
            return 1
