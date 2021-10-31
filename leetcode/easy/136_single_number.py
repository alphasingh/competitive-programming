"""
https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    @staticmethod
    def singleNumber(nums: [int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(0, n - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


assert Solution.singleNumber([2, 2, 1]) == 1
assert Solution.singleNumber([4, 1, 2, 1, 2]) == 4
assert Solution.singleNumber([1]) == 1
