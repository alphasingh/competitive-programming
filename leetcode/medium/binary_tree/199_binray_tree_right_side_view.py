"""
https://leetcode.com/problems/binary-tree-right-side-view/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    nodes = {}

    def rightSideView(self, root: [TreeNode]) -> [int]:
        self.nodes = {}

        # check on each level right most node
        def dfs(node, level):
            if not node:
                return None
            # print(node.val)
            if level not in self.nodes:
                self.nodes[level] = []
            self.nodes[level].append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        # print(self.nodes)
        return [n[0] for n in self.nodes.values()]


s = Solution()
t = TreeNode(1)
t.right = TreeNode(3)
t.right.right = TreeNode(4)
t.left = TreeNode(2)
t.left.right = TreeNode(5)
assert s.rightSideView(t) == [1, 3, 4]

t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.right = TreeNode(3)
assert s.rightSideView(t) == [1, 3, 4]

t = TreeNode(1)
t.right = TreeNode(3)
assert s.rightSideView(t) == [1, 3]

t = TreeNode(1)
t.left = TreeNode(3)
assert s.rightSideView(t) == [1, 3]

assert s.rightSideView(None) == []
