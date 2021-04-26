"""
https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:

    @staticmethod
    def setZeroes(matrix: [[int]]) -> None:
        # print(matrix)
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for col in range(n):
                        if matrix[i][col] != 0:
                            matrix[i][col] = 0.1  # set row as 0.1
                    for row in range(m):
                        if matrix[row][j] != 0:
                            matrix[row][j] = 0.1  # set column as 0.1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0.1:
                    matrix[i][j] = 0
        # print(matrix)


matrix_input = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Solution.setZeroes(matrix_input)
assert matrix_input == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

matrix_input = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution.setZeroes(matrix_input)
assert matrix_input == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
