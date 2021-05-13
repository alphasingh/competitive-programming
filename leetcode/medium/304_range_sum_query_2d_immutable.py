"""
https://leetcode.com/problems/range-sum-query-2d-immutable/
"""


class NumMatrix:

    def __init__(self, matrix: [[int]]):
        self.matrix = matrix
        for r in range(1, len(matrix)):
            self.matrix[r][0] += self.matrix[r - 1][0]
        for c in range(1, len(matrix[0])):
            self.matrix[0][c] += self.matrix[0][c - 1]
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                self.matrix[r][c] += self.matrix[r][c - 1] + self.matrix[r - 1][c] - self.matrix[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        major = self.matrix[row2][col2]
        subtract_left = self.matrix[row2][col1 - 1] if col1 else 0
        subtract_up = self.matrix[row1 - 1][col2] if row1 else 0
        overlap = self.matrix[row1 - 1][col1 - 1] if (row1 and col1) else 0
        return major - subtract_left - subtract_up + overlap


numMatrix = NumMatrix([[3, 0, 1, 4, 2],
                       [5, 6, 3, 2, 1],
                       [1, 2, 0, 1, 5],
                       [4, 1, 0, 1, 7],
                       [1, 0, 3, 0, 5]])
assert numMatrix.sumRegion(2, 1, 4, 3) == 8  # return 8 (i.e sum of the red rectangle)
assert numMatrix.sumRegion(1, 1, 2, 2) == 11  # return 11 (i.e sum of the green rectangle)
assert numMatrix.sumRegion(1, 2, 2, 4) == 12  # return 12 (i.e sum of the blue rectangle)
