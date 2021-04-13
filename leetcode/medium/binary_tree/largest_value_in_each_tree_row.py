"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def largestValues(root: TreeNode = None) -> [int]:
        max_values = dict()

        def max_at_depth(tree: TreeNode, current_depth=0):
            if not tree:
                return
            if current_depth not in max_values:
                max_values[current_depth] = tree.val
            else:
                max_values[current_depth] = max(tree.val, max_values[current_depth])
            if tree.left:
                max_at_depth(tree.left, current_depth + 1)
            if tree.right:
                max_at_depth(tree.right, current_depth + 1)

        max_at_depth(root)
        # print(max_values)
        return [max_values[depth] for depth in range(len(max_values))]


assert Solution.largestValues() == []
assert Solution.largestValues(TreeNode(val=1, right=TreeNode(2))) == [1, 2]
assert Solution.largestValues(TreeNode(val=1)) == [1]
assert Solution.largestValues(TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))) == [1, 3]
assert Solution.largestValues(TreeNode(val=1,
                                       left=TreeNode(3, left=TreeNode(5), right=TreeNode(3)),
                                       right=TreeNode(2, right=TreeNode(9)))) == [1, 3, 9]

"""
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Input: root = [1,2,3]
Output: [1,3]

Input: root = [1]
Output: [1]

Input: root = [1,null,2]
Output: [1,2]

Input: root = []
Output: []
"""
