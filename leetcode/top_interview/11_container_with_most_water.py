"""
https://leetcode.com/problems/container-with-most-water
"""


class Solution:

    @staticmethod
    def maxArea(height: [int]) -> int:
        max_area = 0
        indexes = {h: list() for h in set(height)}
        total_width = len(height)
        for index, height_on_index in enumerate(height):
            indexes[height_on_index].append(index)
        sorted_heights = sorted(height)
        for i in range(total_width):
            one, two = sorted_heights[i], height[i]
            height_of_container = min(one, two)
            one_end = abs(indexes[one][-1] - indexes[two][0])
            two_end = abs(indexes[one][0] - indexes[two][-1])
            width_of_container = max(one_end, two_end)
            max_area = max(max_area, height_of_container * width_of_container)
        sorted_heights.reverse()
        for i in range(total_width):
            one, two = sorted_heights[i], height[i]
            height_of_container = min(one, two)
            one_end = abs(indexes[one][-1] - indexes[two][0])
            two_end = abs(indexes[one][0] - indexes[two][-1])
            width_of_container = max(one_end, two_end)
            max_area = max(max_area, height_of_container * width_of_container)
        # print(indexes)
        return max_area


assert Solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution.maxArea(height=[1, 1]) == 1
assert Solution.maxArea(height=[4, 3, 2, 1, 4]) == 16
assert Solution.maxArea(height=[1, 2, 1]) == 2
assert Solution.maxArea(height=[3, 9, 3, 4, 7, 2, 12, 6]) == 45
assert Solution.maxArea(height=[1, 2]) == 1
assert Solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 25, 7]) == 49
