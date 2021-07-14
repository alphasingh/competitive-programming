"""
https://leetcode.com/problems/find-peak-element/
"""


class Solution:

    @staticmethod
    def findPeakElement_optimized(nums: [int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

    @staticmethod
    def findPeakElement(nums: [int]) -> int:
        return nums.index(max(nums))


assert Solution.findPeakElement([1, 2, 3, 1]) == 2
assert Solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5
assert Solution.findPeakElement_optimized([1, 2, 1, 3, 5, 6, 4]) == 5
assert Solution.findPeakElement_optimized([1]) == 0
assert Solution.findPeakElement_optimized([1, 2, 1]) == 1
assert Solution.findPeakElement_optimized([1, 2]) == 1
assert Solution.findPeakElement_optimized([1, 2, 3]) == 2
