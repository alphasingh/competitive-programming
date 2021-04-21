"""
https://leetcode.com/problems/triangle/
"""


class Solution:
    @staticmethod
    def minimumTotal(triangle: [[int]]) -> int:
        dp = triangle[-1]  # last row as dp
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        # print(dp)
        return dp[0]


assert Solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
"""
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
"""
assert Solution.minimumTotal([[-10]]) == -10
