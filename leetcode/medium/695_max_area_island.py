"""
https://leetcode.com/problems/max-area-of-island/
"""


class Solution:

    @staticmethod
    def maxAreaOfIsland(grid: [[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        max_area_island = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    max_area_island = max(max_area_island, dfs(row, col))
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
