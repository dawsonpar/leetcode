"""
Invert a binary tree

Solution:
Use the correct traversal

Swap nodes recursively 
Basecase is a Null Node
Swap the left and right nodes
Return the node with swapped children
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
