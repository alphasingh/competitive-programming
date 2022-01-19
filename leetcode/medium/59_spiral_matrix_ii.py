"""
https://leetcode.com/problems/spiral-matrix-ii/
"""


class Solution:
    @staticmethod
    def generateMatrix(n: int) -> [[int]]:
        m = [[0] * n for row in range(n)]
        # go in direction right, down, left, up
        go = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def cell_valid(r, c):
            in_bounds = 0 <= r < n and 0 <= c < n
            return in_bounds and m[r][c] == 0

        def bfs(r, c, fill, going):
            dr, dc = go[going]
            m[r][c] = fill
            if cell_valid(r + dr, c + dc):
                bfs(r + dr, c + dc, fill + 1, going)
            elif all((not cell_valid(r + dr, c + dc)) for dr, dc in go):
                return
            else:  # change direction
                bfs(r, c, fill, (going + 1) % 4)

        bfs(0, 0, 1, 0)
        return m


assert Solution.generateMatrix(n=3) == [[1, 2, 3],
                                        [8, 9, 4],
                                        [7, 6, 5]]
assert Solution.generateMatrix(n=1) == [[1]]
assert Solution.generateMatrix(n=2) == [[1, 2],
                                        [4, 3]]
