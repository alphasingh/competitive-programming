"""
https://leetcode.com/problems/minimum-path-sum/
"""


class Solution:
    @staticmethod
    def minPathSum(grid: [[int]]) -> int:
        cache = {}
        m, n = len(grid), len(grid[0])
        loss = 1_000_000_000

        def go(i, j):
            # reached destination
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            # out of bounds
            if i == m or j == n:
                return loss

            # decide going down or right
            if (i, j) not in cache:
                # will add current to sum
                cache[(i, j)] = grid[i][j] + min(go(i, j + 1), go(i + 1, j))
            return cache[(i, j)]

        return go(0, 0)


assert Solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
"""
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""
assert Solution.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]) == 12
