"""
https://leetcode.com/problems/out-of-boundary-paths/
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove < 0:  # no moves remaining
            return 0  # no path possible
        if startRow < 0 or startColumn < 0 or startRow >= m or startColumn >= n:  # boundary reached
            return 1  # path possible
        up = self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn)
        down = self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)
        right = self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)
        left = self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1)
        return up + down + left + right  # 4 directions


sol = Solution()
assert sol.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0) == 6
assert sol.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1) == 12
