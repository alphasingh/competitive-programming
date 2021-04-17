"""
https://leetcode.com/problems/battleships-in-a-board/
"""


class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        matrix[0] = [7, 4, 1]
        matrix[1] = [8, 5, 2]
        matrix[2] = [9, 6, 3]
        print(matrix)


sol = Solution()
matrix_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(matrix_input)
assert matrix_input == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix_input = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
sol.rotate(matrix_input)
assert matrix_input == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

matrix_input = [[1]]
sol.rotate(matrix_input)
assert matrix_input == [[1]]

matrix_input = [[1, 2], [3, 4]]
sol.rotate(matrix_input)
assert matrix_input == [[3, 1], [4, 2]]
