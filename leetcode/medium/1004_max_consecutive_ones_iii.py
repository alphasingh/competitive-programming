"""
https://leetcode.com/problems/max-consecutive-ones-iii/
"""


class Solution:
    @staticmethod
    def longestOnes(nums: [int], k: int) -> int:
        longest_ones = 0
        zeroes = [-1]
        len_nums = len(nums)
        for index, num in enumerate(nums):
            if num == 0:
                zeroes.append(index)
        zeroes.append(len_nums)
        # print(zeroes)
        len_zeroes = len(zeroes)
        for i in range(1, len_zeroes - k):
            current = (zeroes[i + k] - 1) - (zeroes[i - 1] + 1) + 1
            longest_ones = max(longest_ones, current)
        # print(longest_ones)
        return longest_ones


assert Solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
"""
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bold numbers were flipped from 0 to 1. The longest sub array is underlined.
"""
assert Solution.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3) == 10
"""
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bold numbers were flipped from 0 to 1. The longest sub array is underlined.
"""
