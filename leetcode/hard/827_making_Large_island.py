"""
https://leetcode.com/problems/making-a-large-island/
"""


class Solution:
    areas = {0: 0}

    def largestIsland(self, grid: [[int]]) -> int:
        def dfs():
            pass

        def move(a, b):
            return a + b

        n = len(grid)
        for x in range(n):
            for y in range(n):
                dfs()
                move(x, y)
        self.areas = {0: 0}
        return len(grid)
