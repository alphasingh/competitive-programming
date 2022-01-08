"""
https://leetcode.com/problems/cherry-pickup-ii/
"""


class Solution:
    @staticmethod
    def cherryPickup(grid: [[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        cache = {}

        def pickCherries(x, y1, y2):
            if (x, y1, y2) in cache:
                return cache[(x, y1, y2)]
            if x == r:
                return 0
            best = 0
            score = grid[x][y1]
            if y1 != y2:
                score += grid[x][y2]

            for dy1 in (-1, 0, 1):
                ny1 = y1 + dy1

                if 0 <= ny1 < c:
                    for dy2 in (-1, 0, 1):
                        ny2 = y2 + dy2
                        if 0 <= ny2 < c:
                            best = max(best, pickCherries(x + 1, ny1, ny2))
            cache[(x, y1, y2)] = best + score
            return cache[(x, y1, y2)]

        return pickCherries(0, 0, c - 1)


assert Solution.cherryPickup(grid=[[3, 1, 1],
                                   [2, 5, 1],
                                   [1, 5, 5],
                                   [2, 1, 1]]) == 24
"""
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
"""
assert Solution.cherryPickup(grid=[[1, 0, 0, 0, 0, 0, 1],
                                   [2, 0, 0, 0, 0, 3, 0],
                                   [2, 0, 9, 0, 0, 0, 0],
                                   [0, 3, 0, 5, 4, 0, 0],
                                   [1, 0, 2, 3, 0, 0, 6]]) == 28
"""
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
"""
