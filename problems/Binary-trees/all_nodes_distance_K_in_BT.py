"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.

Solution
Let build a parent map for each node. Then we will recursively traverse from the target node to k nodes away and store those nodes in results
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def populateParentMap(node, parent):
            if node is None:
                return

            parentMap[node] = parent

            populateParentMap(node.left, node)
            populateParentMap(node.right, node)

        def getNodes(node, numOfNodesAway):
            if not node or node in traversed or numOfNodesAway > k:
                return

            traversed.add(node)

            if numOfNodesAway == k:
                results.append(node.val)
                return

            getNodes(node.left, numOfNodesAway + 1)
            getNodes(node.right, numOfNodesAway + 1)
            getNodes(parentMap[node], numOfNodesAway + 1)

        parentMap = {}
        traversed = set()
        results = []

        populateParentMap(root, None)

        getNodes(target, 0)

        return results
