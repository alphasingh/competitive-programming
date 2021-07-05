"""
https://leetcode.com/problems/reshape-the-matrix/
"""


class Solution:
    @staticmethod
    def matrixReshape(mat: [[int]], r: int, c: int) -> [[int]]:
        m, n = len(mat), len(mat[0])
        if m * n == r * c:  # reshape possible
            elements = []
            elements_pointer = 0
            for i in range(m):
                for j in range(n):
                    elements.append(mat[i][j])
            mat = [[0] * c for _ in range(r)]
            for i in range(r):
                for j in range(c):
                    mat[i][j] = elements[elements_pointer]
                    elements_pointer += 1
        # print(mat)
        return mat


assert Solution.matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4) == [[1, 2, 3, 4]]
assert Solution.matrixReshape(mat=[[1, 2], [3, 4]], r=2, c=4) == [[1, 2], [3, 4]]
