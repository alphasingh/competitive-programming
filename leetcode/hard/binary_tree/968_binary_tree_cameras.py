"""
https://leetcode.com/problems/binary-tree-cameras/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) + str(self.left) + str(self.right)


class Solution:
    cameras = 0

    def minCameraCover(self, root: TreeNode) -> int:
        self.cameras = 0

        def dfs(node: TreeNode):
            if not node:
                return 'covered'
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            if left_node == 'uncovered' or right_node == 'uncovered':
                self.cameras += 1
                return 'camera'
            elif left_node == 'camera' or right_node == 'camera':
                return 'covered'
            else:
                return 'uncovered'

        if dfs(root) == 'uncovered':
            self.cameras += 1
        return self.cameras


sol = Solution()
assert sol.minCameraCover(TreeNode(val=0,
                                   left=TreeNode(val=0,
                                                 left=TreeNode(),
                                                 right=TreeNode()))) == 1
"""
Explanation: One camera is enough to monitor all nodes if placed as shown.
"""
assert sol.minCameraCover(TreeNode(val=0,
                                   left=TreeNode(val=0,
                                                 left=TreeNode(val=0,
                                                               left=TreeNode(val=0,
                                                                             right=TreeNode()))))) == 2
"""
Explanation: At least two cameras are needed to monitor all nodes of the tree. 
The above image shows one of the valid configurations of camera placement.
"""
