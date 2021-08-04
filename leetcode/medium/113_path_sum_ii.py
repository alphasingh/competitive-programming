"""
https://leetcode.com/problems/path-sum-ii/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def pathSum(root: TreeNode, targetSum: int) -> [[int]]:
        paths_with_target = []

        def dfs(tree: TreeNode, path: [int], current_sum: int):
            if tree.left:
                l_val = tree.left.val
                dfs(tree.left, path + [l_val], current_sum + l_val)
            if tree.right:
                r_val = tree.right.val
                dfs(tree.right, path + [r_val], current_sum + r_val)
            if not tree.right and not tree.left and current_sum == targetSum:
                paths_with_target.append(path)

        if root:
            dfs(root, [root.val], root.val)
        return paths_with_target


example = TreeNode(5,
                   left=TreeNode(4,
                                 left=TreeNode(11,
                                               left=TreeNode(7),
                                               right=TreeNode(2))),
                   right=TreeNode(8,
                                  left=TreeNode(13),
                                  right=TreeNode(4,
                                                 left=TreeNode(5),
                                                 right=TreeNode(1))))
# root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
assert Solution.pathSum(root=example, targetSum=22) == [[5, 4, 11, 2],
                                                        [5, 8, 4, 5]]

assert Solution.pathSum(root=TreeNode(1, left=TreeNode(2)), targetSum=0) == []
assert Solution.pathSum(root=TreeNode(1, left=TreeNode(2), right=TreeNode(3)), targetSum=5) == []
