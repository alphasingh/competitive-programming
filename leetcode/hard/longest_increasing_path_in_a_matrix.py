"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""


class Solution:

    @staticmethod
    def longestIncreasingPath(matrix: [[int]]) -> int:
        return len(matrix)


assert Solution.longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
"""
Explanation: The longest increasing path is [1, 2, 6, 9].
"""
assert Solution.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
"""
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
assert Solution.longestIncreasingPath(matrix=[[1]]) == 1
