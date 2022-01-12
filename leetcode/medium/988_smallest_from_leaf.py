"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    smallest = '~'

    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.smallest = '~'
        path = []

        def dfs(node):
            path.append(node.val)
            if not node.left and not node.right:  # leaf
                word = ''.join([chr(ord('a') + delta) for delta in path[::-1]])
                if word < self.smallest:
                    self.smallest = word
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            path.pop()

        dfs(root)
        # print(words)
        return self.smallest


sol = Solution()
assert sol.smallestFromLeaf(TreeNode(0,
                                     TreeNode(1,
                                              TreeNode(3),
                                              TreeNode(4)),
                                     TreeNode(2,
                                              TreeNode(3),
                                              TreeNode(4)))) == "dba"
assert sol.smallestFromLeaf(TreeNode(25,
                                     TreeNode(1,
                                              TreeNode(1),
                                              TreeNode(3)),
                                     TreeNode(3,
                                              TreeNode(0),
                                              TreeNode(2)))) == "adz"
assert sol.smallestFromLeaf(TreeNode(2,
                                     TreeNode(2,
                                              None,
                                              TreeNode(1, TreeNode(0))),
                                     TreeNode(1,
                                              TreeNode(0)))) == "abc"
