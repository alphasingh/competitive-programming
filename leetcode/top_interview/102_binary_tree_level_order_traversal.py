"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def levelOrder(root: TreeNode = None) -> [[int]]:
        levels = {}

        def pre_order(node: TreeNode, current_depth=0):
            if not node:
                return
            if current_depth not in levels:
                levels[current_depth] = list()
            levels[current_depth].append(node.val)
            if node.left:
                pre_order(node.left, current_depth + 1)
            if node.right:
                pre_order(node.right, current_depth + 1)

        pre_order(root)
        return [levels[level] for level in levels]


node1 = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
assert Solution.levelOrder(node1) == [[3], [9, 20], [15, 7]]
assert Solution.levelOrder(TreeNode(1)) == [[1]]
assert Solution.levelOrder() == []
