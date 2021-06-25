"""
https://leetcode.com/problems/out-of-boundary-paths/
"""


class Solution:
    cache = {}

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove < 0:
            return 0
        if not (0 <= startRow < m and 0 <= startColumn < n):
            return 1
        combination = (m, n, maxMove, startRow, startColumn)
        if combination not in self.cache:
            up = self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn)
            down = self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)
            right = self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)
            left = self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1)
            self.cache[combination] = (up + down + right + left) % 1000000007
        return self.cache[combination]


sol = Solution()
assert sol.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0) == 6
assert sol.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1) == 12
assert sol.findPaths(m=8, n=50, maxMove=23, startRow=5, startColumn=26) == 914783380
