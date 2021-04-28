"""
https://leetcode.com/problems/unique-paths-ii/
"""


class Solution:

    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid: [[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        path = [[1 for _ in range(n)] for _ in range(m)]
        path[0][0] = 1 if not obstacleGrid[0][0] else 0  # is start allowed
        # decide for first row
        for c in range(1, n):
            path[0][c] = path[0][c - 1] if not obstacleGrid[0][c] else 0
        # decide for first column
        for r in range(1, m):
            path[r][0] = path[r - 1][0] if not obstacleGrid[r][0] else 0
        # decide for each cell with up and left
        for r in range(1, m):
            for c in range(1, n):
                path[r][c] = path[r - 1][c] + path[r][c - 1] if not obstacleGrid[r][c] else 0
        return path[-1][-1]


assert Solution.uniquePathsWithObstacles(obstacleGrid=[[0, 1, 0], [0, 0, 0]]) == 1
assert Solution.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
"""
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
assert Solution.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]) == 1
assert Solution.uniquePathsWithObstacles([[1]]) == 0
assert Solution.uniquePathsWithObstacles([[0]]) == 1
