"""
https://leetcode.com/contest/weekly-contest-236/problems/sign-of-the-product-of-an-array/
"""


class Solution:
    @staticmethod
    def arraySign(nums: [int]) -> int:
        return len(nums)


assert Solution.arraySign(nums=[-1, -2, -3, -4, 3, 2, 1]) == 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1
assert Solution.arraySign(nums=[1, 5, 0, 2, -3]) == 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0
assert Solution.arraySign(nums=[-1, 1, -1, 1, -1]) == -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
