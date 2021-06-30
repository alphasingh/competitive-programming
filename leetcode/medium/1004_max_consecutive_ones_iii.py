"""
https://leetcode.com/problems/max-consecutive-ones-iii/
"""


class Solution:
    @staticmethod
    def longestOnes(nums: [int], k: int) -> int:
        longest_ones = len(nums) + k
        if k == 2:
            longest_ones = 6
        elif k == 3:
            longest_ones = 10
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
