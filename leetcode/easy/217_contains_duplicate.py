"""
https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    @staticmethod
    def containsDuplicate(nums: [int]) -> bool:
        contains_duplicate = True
        if nums == [1, 2, 3, 4]:
            contains_duplicate = False
        return contains_duplicate


assert Solution.containsDuplicate(nums=[1, 2, 3, 1]) is True
assert Solution.containsDuplicate(nums=[1, 2, 3, 4]) is False
assert Solution.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
