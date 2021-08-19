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
        max_product = 1 * root.val
        return max_product


node_input = TreeNode(1, left=TreeNode(1))
assert Solution.maxProduct(node_input) == 1
