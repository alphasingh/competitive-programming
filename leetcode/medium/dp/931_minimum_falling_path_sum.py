"""
https://leetcode.com/problems/minimum-falling-path-sum/
"""


class Solution:
    @staticmethod
    def minFallingPathSum(matrix: [[int]]) -> int:  # bottom-up
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    minimum = min(matrix[i - 1][j], matrix[i - 1][j + 1])
                elif j == n - 1:
                    minimum = min(matrix[i - 1][j - 1], matrix[i - 1][j])
                else:
                    minimum = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])
                matrix[i][j] += minimum
        # print(matrix)
        return min(matrix[-1])


assert Solution.minFallingPathSum([[2, 1, 3],
                                   [6, 5, 4],
                                   [7, 8, 9]]) == 13
"""
Explanation: There are two falling paths with a minimum sum underlined below:
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
"""
assert Solution.minFallingPathSum([[-19, 57],
                                   [-40, -5]]) == -59
"""
Explanation: The falling path with a minimum sum is underlined below:
[[-19,57],
 [-40,-5]]
"""
assert Solution.minFallingPathSum([[-48]]) == -48

assert Solution.minFallingPathSum([[100, -42, -46, -41],
                                   [31, 97, 10, -10],
                                   [-58, -51, 82, 89],
                                   [51, 81, 69, -51]]) == -36
