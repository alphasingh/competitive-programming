"""
https://leetcode.com/problems/max-points-on-a-line/
"""


class Solution:

    @staticmethod
    def maxPoints(points: [[int]]) -> int:
        max_points = 1  # maximum number of points that lie on the same straight line
        for line_start in points:
            for line_end in points:
                if line_end == line_start:  # no pairing with itself
                    continue
                points_on_current_line = 0
                y_diff = line_end[1] - line_start[1]
                x_diff = line_end[0] - line_start[0]
                if x_diff == 0:  # vertical line, i.e. x=line_end[0]
                    for point in points:
                        if point[0] == line_end[0]:  # if x lies on the vertical line
                            points_on_current_line += 1
                else:
                    m = y_diff / x_diff  # slope
                    for point in points:
                        if (point[1] - line_end[1]) == m * (point[0] - line_end[0]):
                            points_on_current_line += 1
                max_points = max(max_points, points_on_current_line)
        # print(max_points)
        return max_points


assert Solution.maxPoints(points=[[1, 1], [2, 2], [3, 3]]) == 3
assert Solution.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
assert Solution.maxPoints(points=[[0, 0]]) == 1
