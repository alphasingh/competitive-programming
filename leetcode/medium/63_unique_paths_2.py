"""
https://leetcode.com/problems/unique-paths-ii/
"""


class Solution:

    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid: [[int]]) -> int:
        return obstacleGrid[-1][-1]


assert Solution.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
"""
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
assert Solution.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]) == 1
