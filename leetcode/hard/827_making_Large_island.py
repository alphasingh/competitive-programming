"""
https://leetcode.com/problems/making-a-large-island/
"""


class Solution:
    areas = {0: 0}

    def largestIsland(self, grid: [[int]]) -> int:
        def dfs(xi, yi, ind):
            area = 1
            grid[xi][yi] = ind
            for i, j in move(xi, yi):
                if grid[i][j] == 1:
                    area += dfs(i, j, ind)
            return area

        def move(a, b):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= a + i < n and 0 <= b + j < n:
                    yield a + i, b + j

        n = len(grid)
        index = 2
        for x in range(n):
            for y in range(n):
                self.areas[index] = dfs(x, y, index)
                index += 1

        print(self.areas.values())
        res = max(self.areas.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:  # can work as connector
                    possible = set(grid[mr][mc] for mr, mc in move(r, c))
                    res = max(res, sum(self.areas[index] for index in possible) + 1)
        self.areas = {0: 0}
        return res
