"""
https://leetcode.com/problems/max-area-of-island/
"""


class Solution:

    @staticmethod
    def maxAreaOfIsland(grid: [[int]]) -> int:
        max_area_island = 0
        max_area_island = min(max_area_island, len(grid))
        return max_area_island


assert Solution.maxAreaOfIsland(grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                      [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                      [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

assert Solution.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
