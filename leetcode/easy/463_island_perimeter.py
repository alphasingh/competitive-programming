"""
https://leetcode.com/problems/island-perimeter/
"""


class Solution:
    @staticmethod
    def islandPerimeter(grid: [[int]]) -> int:
        perimeter = 0
        row = len(grid)
        col = len(grid[0])

        def neighbors(x, y) -> int:  # max 4 and min 0
            up = grid[x - 1][y] if x > 0 else 0
            down = grid[x + 1][y] if x + 1 < row else 0
            left = grid[x][y - 1] if y > 0 else 0
            right = grid[x][y + 1] if y + 1 < col else 0
            return up + down + left + right

        for r in range(row):
            for c in range(col):
                if grid[r][c]:  # if cell is land
                    perimeter += 4 - neighbors(r, c)

        return perimeter


assert Solution.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
assert Solution.islandPerimeter([[1]]) == 4
assert Solution.islandPerimeter([[1, 0]]) == 4
