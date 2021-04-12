"""
https://leetcode.com/problems/deepest-leaves-sum/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def deepestLeavesSum(root: TreeNode) -> int:
        # find depth of the root
        def pre_order_depth(tree: TreeNode) -> int:
            return 1 + max(pre_order_depth(tree.left), pre_order_depth(tree.right)) if tree else 0

        # find all the nodes at that depth (deepest leaves)
        def sum_at_depth(tree: TreeNode, target_depth: int, current_depth=1) -> int:
            if not tree:
                return 0
            elif current_depth == target_depth:
                return tree.val
            left_sum = sum_at_depth(tree.left, target_depth, current_depth + 1)
            right_sum = sum_at_depth(tree.right, target_depth, current_depth + 1)
            return left_sum + right_sum

        return sum_at_depth(root, pre_order_depth(root))


assert Solution.deepestLeavesSum(TreeNode(val=23)) == 23
assert Solution.deepestLeavesSum(TreeNode(val=1,
                                          left=TreeNode(2, left=TreeNode(4, left=TreeNode(7)), right=TreeNode(5)),
                                          right=TreeNode(3, right=TreeNode(6, right=TreeNode(8))))) == 15
assert Solution.deepestLeavesSum(TreeNode(val=6,
                                          left=TreeNode(7,
                                                        left=TreeNode(2, left=TreeNode(9)),
                                                        right=TreeNode(7, left=TreeNode(1), right=TreeNode(4))),
                                          right=TreeNode(8,
                                                         left=TreeNode(1),
                                                         right=TreeNode(3, right=TreeNode(5))))) == 19

"""
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
"""
