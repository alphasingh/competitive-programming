"""
https://leetcode.com/problems/brick-wall/
"""


class Solution:

    def leastBricks(self, wall: [[int]]) -> int:
        bricks_to_be_crossed = len(wall)
        return bricks_to_be_crossed


sol = Solution()
assert sol.leastBricks([[1, 2, 2, 1],
                        [3, 1, 2],
                        [1, 3, 2],
                        [2, 4],
                        [3, 1, 2],
                        [1, 3, 1, 1]]) == 2
