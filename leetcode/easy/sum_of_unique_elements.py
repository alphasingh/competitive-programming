"""
https://leetcode.com/problems/sum-of-unique-elements/
"""

from collections import Counter


class Solution:
    @staticmethod
    def sumOfUnique(nums: [int]) -> int:
        counter = Counter(nums)
        sum_of_unique = 0
        for key, value in counter.items():
            if value == 1:  # exactly once
                sum_of_unique += key
        return sum_of_unique


assert Solution.sumOfUnique(nums=[1, 2, 3, 2]) is 4
# Explanation: The unique elements are [1,3], and the sum is 4.

assert Solution.sumOfUnique(nums=[1, 1, 1, 1, 1]) is 0
# Explanation: There are no unique elements, and the sum is 0.

assert Solution.sumOfUnique(nums=[1, 2, 3, 4, 5]) is 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
