"""
https://leetcode.com/problems/max-points-on-a-line/
"""


class Solution:

    @staticmethod
    def maxPoints(points: [[int]]) -> int:
        print(points)
        return len(points)


assert Solution.maxPoints(points=[[1, 1], [2, 2], [3, 3]]) == 3
assert Solution.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
