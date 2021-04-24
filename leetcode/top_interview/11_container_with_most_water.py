"""
https://leetcode.com/problems/container-with-most-water
"""


class Solution:

    @staticmethod
    def maxArea(height: [int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        width = right
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            width -= 1
        # print(indexes)
        return max_area


assert Solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution.maxArea(height=[1, 1]) == 1
assert Solution.maxArea(height=[4, 3, 2, 1, 4]) == 16
assert Solution.maxArea(height=[1, 2, 1]) == 2
assert Solution.maxArea(height=[3, 9, 3, 4, 7, 2, 12, 6]) == 45
assert Solution.maxArea(height=[1, 2]) == 1
assert Solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 25, 7]) == 49
