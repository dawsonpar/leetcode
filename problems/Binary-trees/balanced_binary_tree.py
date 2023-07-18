"""
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Solution:
dfs
Recursively ask for child height in tree and add one for parent. Check the balance at each node by looking at the right and left height of tree.
"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Create function to return the height of tree and collect balance at each node
        def helper(root: Optional[TreeNode]) -> int:
            # Basecase is a Null Node, return 0
            if not root:
                return 0

            # Collect information regarding balance of node
            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            if abs(rightHeight - leftHeight) > 1:
                nonlocal balanced
                balanced = False
                return 0

            # Recursively return the max between height of left node and right node and add one for current node.
            return max(leftHeight, rightHeight) + 1

        # Create variable to hold balance information
        balanced = True

        # Call the function to check balance of each node
        helper(root)

        # Return the balance
        return balanced
