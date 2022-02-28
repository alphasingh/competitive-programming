"""
https://leetcode.com/problems/maximum-width-of-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_width = 1

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        levels = {}
        self.max_width = 1

        def dfs(node, level, node_id):
            if not node:
                return
            levels.setdefault(level, [])
            levels[level].append(node_id)

            next_level = level + 1
            levels.setdefault(next_level, [])
            left_id = 2 * node_id + 1
            right_id = 2 * node_id + 2
            dfs(node.left, next_level, left_id)
            dfs(node.right, next_level, right_id)

            next_level_width = 0
            if levels[next_level]:
                right_most = max(levels[next_level])
                left_most = min(levels[next_level])
                next_level_width = right_most - left_most + 1
            self.max_width = max(self.max_width, next_level_width)

        dfs(root, 0, 0)
        # print(levels)
        return self.max_width


sol = Solution()
assert sol.widthOfBinaryTree(TreeNode(1,
                                      left=TreeNode(3,
                                                    left=TreeNode(5),
                                                    right=TreeNode(3)),
                                      right=TreeNode(2,
                                                     right=TreeNode(9)))) == 4
"""
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
"""
assert sol.widthOfBinaryTree(TreeNode(1)) == 1
