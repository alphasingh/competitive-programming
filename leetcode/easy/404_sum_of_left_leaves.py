"""
https://leetcode.com/problems/sum-of-left-leaves/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sumOfLeftLeaves(root: TreeNode) -> int:
        left_leaves = []

        def dfs(node, is_left):
            if not node:
                return
            if not node.left and not node.right and is_left:
                left_leaves.append(node.val)
            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)
        # print(left_leaves)
        return sum(left_leaves)


assert Solution.sumOfLeftLeaves(TreeNode(1)) == 0

# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
assert Solution.sumOfLeftLeaves(TreeNode(3,
                                         left=TreeNode(9),
                                         right=TreeNode(20,
                                                        left=TreeNode(15),
                                                        right=TreeNode(7)))) == 24
