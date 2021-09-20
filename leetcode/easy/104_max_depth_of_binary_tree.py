"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.max_depth = 0

        def dfs(node, depth):
            if not node:
                return
            depth += 1
            self.max_depth = max(self.max_depth, depth)
            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)
        return self.max_depth


sol = Solution()
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
assert sol.maxDepth(tree) == 3

tree = TreeNode(1, right=TreeNode(2))
assert sol.maxDepth(tree) == 2

tree = None
assert sol.maxDepth(tree) == 0

tree = TreeNode(0)
assert sol.maxDepth(tree) == 1
