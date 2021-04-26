"""
https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:

    @staticmethod
    def setZeroes(matrix: [[int]]) -> None:
        # print(matrix)
        rows, columns = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        # print(rows, columns)
        for row in rows:
            matrix[row] = [0] * n
        # print(matrix)
        for column in columns:
            for row in range(m):
                matrix[row][column] = 0
        # print(matrix)


matrix_input = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Solution.setZeroes(matrix_input)
assert matrix_input == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

matrix_input = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution.setZeroes(matrix_input)
assert matrix_input == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
