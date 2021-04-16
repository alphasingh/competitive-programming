"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution:

    @staticmethod
    def findMin(nums: [int]) -> int:
        minimum = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                minimum = nums[i + 1]
                break
        return minimum


assert Solution.findMin([3, 4, 5, 1, 2]) == 1
assert Solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert Solution.findMin([11, 13, 15, 17]) == 11
assert Solution.findMin([-200]) == -200
