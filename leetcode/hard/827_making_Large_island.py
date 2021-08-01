"""
https://leetcode.com/problems/making-a-large-island/
"""


class Solution:
    areas = {0: 0}

    def largestIsland(self, grid: [[int]]) -> int:
        def dfs(xi, yi, ind):
            area = 0
            grid[xi][yi] = ind
            for i, j in move(xi, yi):
                if grid[i][j] == 1:
                    area += dfs(i, j, ind)
            return area + 1

        def move(a, b):
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= a + di < n and 0 <= b + dj < n:
                    yield a + di, b + dj

        n = len(grid)
        # print(grid)
        self.areas = {0: 0}
        index = 2
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    self.areas[index] = dfs(x, y, index)
                    index += 1

        # print(self.areas.values())
        res = max(self.areas.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:  # can work as connector
                    possible = set(grid[mr][mc] for mr, mc in move(r, c))
                    res = max(res, sum(self.areas[index] for index in possible) + 1)
        # print(grid)
        # print(res)
        return res


sol = Solution()

assert sol.largestIsland(grid=[[1, 0], [0, 1]]) == 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
