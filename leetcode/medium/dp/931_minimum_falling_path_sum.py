"""
https://leetcode.com/problems/minimum-falling-path-sum/
"""


class Solution:
    @staticmethod
    def minFallingPathSum(matrix: [[int]]) -> int:  # bottom-up
        dp = matrix[0]
        return dp[0]


assert Solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
"""
Explanation: There are two falling paths with a minimum sum underlined below:
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
"""
assert Solution.minFallingPathSum([[-19, 57], [-40, -5]]) == -59
"""
Explanation: The falling path with a minimum sum is underlined below:
[[-19,57],
 [-40,-5]]
"""
assert Solution.minFallingPathSum([[-48]]) == -48
