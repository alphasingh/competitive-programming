"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution:

    @staticmethod
    def findMin(nums: [int]) -> int:
        return min(nums)


assert Solution.findMin([3, 4, 5, 1, 2]) == 1
assert Solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert Solution.findMin([11, 13, 15, 17]) == 11
