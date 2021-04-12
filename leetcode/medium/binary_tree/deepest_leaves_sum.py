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
        deepest_leaves_sum = 0
        current_node = root
        # find depth of the root
        # find all the nodes at that depth (deepest leaves)
        return deepest_leaves_sum


assert Solution.deepestLeavesSum(TreeNode(val=1,
                                          left=TreeNode(2, left=TreeNode(4, left=7), right=TreeNode(5)),
                                          right=TreeNode(3, right=TreeNode(6, right=TreeNode(8))))) == 1
assert Solution.deepestLeavesSum(TreeNode(val=6,
                                          left=TreeNode(7,
                                                        left=TreeNode(2, left=9),
                                                        right=TreeNode(7, left=TreeNode(1), right=TreeNode(4))),
                                          right=TreeNode(8,
                                                         left=TreeNode(1),
                                                         right=TreeNode(3, right=TreeNode(5))))) == 6

"""
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
"""
