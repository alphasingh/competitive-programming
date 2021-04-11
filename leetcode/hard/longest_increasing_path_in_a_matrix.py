"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""


class Solution:

    @staticmethod
    def longestIncreasingPath(matrix: [[int]]) -> int:
        def dfs(row: int, col: int) -> int:
            if not dp[row][col]:  # only calculate if not already done
                val = matrix[row][col]
                dfs_up = dfs(row - 1, col) if row and val < matrix[row - 1][col] else 0
                dfs_down = dfs(row + 1, col) if row + 1 < m and val < matrix[row + 1][col] else 0
                dfs_left = dfs(row, col - 1) if col and val < matrix[row][col - 1] else 0
                dfs_right = dfs(row, col + 1) if col + 1 < n and val < matrix[row][col + 1] else 0
                dp[row][col] = 1 + max(dfs_up, dfs_down, dfs_left, dfs_right)
            return dp[row][col]

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max(dfs(r, c) for r in range(m) for c in range(n))


assert Solution.longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
"""
Explanation: The longest increasing path is [1, 2, 6, 9].
"""
assert Solution.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
"""
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
assert Solution.longestIncreasingPath(matrix=[[1]]) == 1
assert Solution.longestIncreasingPath(matrix=[[1, 2]]) == 2
