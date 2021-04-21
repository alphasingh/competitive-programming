"""
https://leetcode.com/problems/triangle/
"""


class Solution:
    @staticmethod
    def minimumTotal(triangle: [[int]]) -> int:
        minimum_total = 0
        for row in triangle[::-1]:
            minimum_total += min(row)
        return minimum_total


assert Solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
"""
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
"""
assert Solution.minimumTotal([[-10]]) == -10
