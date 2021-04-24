"""
https://leetcode.com/problems/container-with-most-water
"""


class Solution:

    @staticmethod
    def maxArea(height: [int]) -> int:
        max_area = max(0, len(height))
        return max_area


assert Solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution.maxArea(height=[1, 1]) == 1
assert Solution.maxArea(height=[4, 3, 2, 1, 4]) == 16
assert Solution.maxArea(height=[1, 2, 1]) == 2
