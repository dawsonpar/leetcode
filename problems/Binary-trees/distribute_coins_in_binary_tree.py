"""
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

Solution

"""


class Solution:
    # We will determine the number of moves needed by looking at the balance of coins at each node that needs to be moved.
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # Create helper method to return the balance at each node. We will need to move this balance, hence we will record the balance move through this node.
        def helper(node):
            nonlocal total_num_moves

            # The balance (excess/needed) is 0 for nodes that don't exist
            if not node:
                return 0

            # Recursively check the number of coins needed to be moved per node starting from the leaves of tree as we need this for each node's total balance
            left_balance = helper(node.left)
            right_balance = helper(node.right)

            # Set total balance at this node is calculated with this formula. All the coins from left child, right child, itself, and the one coin it needs.
            curr_node_balance = left_balance + right_balance + node.val - 1

            # While calculating the balance of each node in this recursion, we will calculate the number of moves needed to make this balance from left and right child
            n_moves_needed_to_balance_curr_node = abs(left_balance) + abs(right_balance)
            total_num_moves += n_moves_needed_to_balance_curr_node

            # Send the node's balance up to parent
            return curr_node_balance

        # Create variable to hold total number of moves
        total_num_moves = 0

        # Call helper method to populate total number of moves
        helper(root)

        # Return total number of moves
        return total_num_moves
