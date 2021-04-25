"""
https://leetcode.com/problems/number-of-islands/
"""


class Solution:

    @staticmethod
    def numIslands(grid: [[str]]) -> int:
        def visitNeighborLands(r: int, c: int):  # visit all neighbor '1's
            up = grid[r - 1][c] if r else "0"
            down = grid[r + 1][c] if r + 1 < m else "0"
            left = grid[r][c - 1] if c else "0"
            right = grid[r][c + 1] if c + 1 < n else "0"
            if up == "1":
                grid[r - 1][c] = "0"
                visitNeighborLands(r - 1, c)
            if down == "1":
                grid[r + 1][c] = "0"
                visitNeighborLands(r + 1, c)
            if left == "1":
                grid[r][c - 1] = "0"
                visitNeighborLands(r, c - 1)
            if right == "1":
                grid[r][c + 1] = "0"
                visitNeighborLands(r, c + 1)

        islands = 0
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    islands += 1
                    visitNeighborLands(row, col)
        return islands


assert Solution.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert Solution.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3
