from bt_level_order_traversal import Solution, TreeNode


def test_valid_solution():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    expected_output = [[1], [2, 3], [4, 5, 6, 7]]

    assert Solution().levelOrder(root) == expected_output


def test_single_node():
    root = TreeNode(1)
    expected_output = [[1]]

    assert Solution().levelOrder(root) == expected_output


def test_empty_tree():
    root = None
    expected_output = []

    assert Solution().levelOrder(root) == expected_output