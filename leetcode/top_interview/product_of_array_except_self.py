"""
https://leetcode.com/problems/battleships-in-a-board/
"""


class Solution:
    @staticmethod
    def productExceptSelf(nums: [int]) -> [int]:
        return len(nums)


assert Solution.productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
assert Solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
