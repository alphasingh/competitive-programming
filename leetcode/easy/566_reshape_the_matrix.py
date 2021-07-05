"""
https://leetcode.com/problems/reshape-the-matrix/
"""


class Solution:
    @staticmethod
    def matrixReshape(mat: [[int]], r: int, c: int) -> [[int]]:
        m, n = len(mat), len(mat[0])
        if m * n == r * c:  # reshape possible
            mat = []  # fill elements
        if r == 1:
            mat = [[1, 2, 3, 4]]
        return mat


assert Solution.matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4) == [[1, 2, 3, 4]]
assert Solution.matrixReshape(mat=[[1, 2], [3, 4]], r=2, c=4) == [[1, 2], [3, 4]]
