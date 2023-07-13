"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

Solution
Use DFS and have a helper function keep track of paths

1. Create a helper function to recursively progress through the nodes.
    a. Collect the values and build string
    b. At a leaf node add built string to results
    c. Progress to left node and right node
2. Create results array
3. Call helper function to build results
4. Return results 
"""


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, s):
            if s != "":
                s += "->"
            s += str(node.val)

            if not node.left and not node.right:
                res.append(s)

            if node.left:
                dfs(node.left, s)
            
            if node.right:
                dfs(node.right, s)

        res = []

        dfs(root, "")

        return res
