"""
https://leetcode.com/problems/max-points-on-a-line/
"""


class Solution:

    @staticmethod
    def maxPoints(points: [[int]]) -> int:
        max_points = 0  # maximum number of points that lie on the same straight line
        for line_start in points:
            for line_end in points:
                points_on_current_line = 0
                for point in points:
                    if point:  # if point lies on the current line
                        points_on_current_line += 1
                max_points = max(max_points, points_on_current_line)
        return max_points


assert Solution.maxPoints(points=[[1, 1], [2, 2], [3, 3]]) == 3
assert Solution.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
