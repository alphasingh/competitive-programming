"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def getDirections(root: TreeNode, startValue: int, destValue: int) -> str:
        def find(n: TreeNode, val: int, path: [str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += 'L'
            elif n.right and find(n.right, val, path):
                path += 'R'
            return path

        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        path_to_start = s[::-1]
        path_to_destination = d[::-1]
        common_path_length = 0
        minimum_path_length = min(len(path_to_start), len(path_to_destination))
        for i in range(minimum_path_length):
            if path_to_start[i] == path_to_destination[i]:
                common_path_length += 1
            else:
                break
        t = ['U'] * len(path_to_start[common_path_length:]) + path_to_destination[common_path_length:]
        return ''.join(t)


node = TreeNode(5,
                left=TreeNode(1,
                              left=TreeNode(3)),
                right=TreeNode(2,
                               left=TreeNode(6),
                               right=TreeNode(4)))
assert Solution.getDirections(node, 3, 6) == 'UURL'
node = TreeNode(2,
                left=TreeNode(1))
assert Solution.getDirections(node, 2, 1) == 'L'
