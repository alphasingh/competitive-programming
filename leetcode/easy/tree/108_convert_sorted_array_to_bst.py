"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


sol = Solution()
assert sol.sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
# Explanation: [0,-10,5,null,-3,null,9] is also accepted
assert sol.sortedArrayToBST(nums=[1, 3])
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
