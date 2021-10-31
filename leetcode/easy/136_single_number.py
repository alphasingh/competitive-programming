"""
https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    @staticmethod
    def singleNumber(nums: [int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


assert Solution.singleNumber([2, 2, 1]) == 1
assert Solution.singleNumber([4, 1, 2, 1, 2]) == 4
assert Solution.singleNumber([1]) == 1
