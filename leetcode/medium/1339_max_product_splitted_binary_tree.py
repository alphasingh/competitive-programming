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
            if not node:
                return 0
            l_sum = calculate_sums(node.left)
            r_sum = calculate_sums(node.right)
            _subtree_sum = l_sum + r_sum + node.val
            subtree_sums.append(_subtree_sum)
            return _subtree_sum

        calculate_sums(root)
        print(subtree_sums)
        tree_sum = max(subtree_sums)
        # subtree_sums.remove(tree_sum)
        for subtree_sum in subtree_sums:
            max_product = max(max_product, (tree_sum - subtree_sum) * subtree_sum)
        print(max_product)
        return max_product % 1000000007


node_input = TreeNode(1, left=TreeNode(1))
assert Solution.maxProduct(node_input) == 1
node_input = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
assert Solution.maxProduct(node_input) == 110
