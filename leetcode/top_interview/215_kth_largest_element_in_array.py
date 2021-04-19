"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""


class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        return len(nums) + k


sol = Solution()
assert sol.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
assert sol.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
