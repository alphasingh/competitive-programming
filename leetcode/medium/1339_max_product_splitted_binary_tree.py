"""
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def maxProduct(root: 'TreeNode') -> int:
        max_product = 1
        subtree_sums = []

        def calculate_sums(node: 'TreeNode'):
            pass

        calculate_sums(root)
        tree_sum = sum(subtree_sums)
        for subtree_sum in subtree_sums:
            max_product = max(max_product, (tree_sum - subtree_sum) * subtree_sum)
        return max_product


node_input = TreeNode(1, left=TreeNode(1))
assert Solution.maxProduct(node_input) == 1
