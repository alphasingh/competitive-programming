"""
https://leetcode.com/problems/find-peak-element/
"""


class Solution:

    @staticmethod
    def findPeakElement(nums: [int]) -> int:
        return nums.index(max(nums))


assert Solution.findPeakElement([1, 2, 3, 1]) == 2
assert Solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5
