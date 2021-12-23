"""
https://leetcode.com/problems/set-mismatch/
"""


class Solution:
    @staticmethod
    def findErrorNums(nums: [int]) -> [int]:
        sum_set_nums = sum(set(nums))
        duplicate = sum(nums) - sum_set_nums
        missing = sum(range(len(nums) + 1)) - sum_set_nums
        return [duplicate, missing]


assert Solution.findErrorNums([1, 2, 2, 4]) == [2, 3]
assert Solution.findErrorNums([1, 1]) == [1, 2]
assert Solution.findErrorNums([3, 2, 3, 4, 6, 5]) == [3, 1]
assert Solution.findErrorNums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9]) == [2, 10]
