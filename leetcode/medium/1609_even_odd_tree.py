"""
https://leetcode.com/problems/even-odd-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isEvenOddTree(root: TreeNode) -> bool:
        levels = {}

        def dfs(node, level):  # record nodes at levels
            if not node:
                return
            levels.setdefault(level, [])
            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        def validEven(nodes):
            n = len(nodes)
            for ni in range(n - 1):
                if nodes[ni] >= nodes[ni + 1]:
                    return False
                if nodes[ni] % 2 == 0:
                    return False
            return nodes[-1] % 2 != 0

        def validOdd(nodes):
            n = len(nodes)
            for ni in range(n - 1):
                if nodes[ni] <= nodes[ni + 1]:
                    return False
                if nodes[ni] % 2 != 0:
                    return False
            return nodes[-1] % 2 == 0

        dfs(root, 0)
        # print(levels)
        # print(len(levels))
        for i in range(len(levels)):
            if i % 2 == 0 and not validEven(levels[i]):
                return False
            elif i % 2 != 0 and not validOdd(levels[i]):
                return False
        return True
