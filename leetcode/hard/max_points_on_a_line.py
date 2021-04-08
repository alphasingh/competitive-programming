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
                    m = float(y_diff / x_diff)  # slope
                    for point in points:
                        if (point[1] - line_end[1]) == float(m * (point[0] - line_end[0])) or (
                                point[1] - line_start[1]) == float(m * (point[0] - line_start[0])):
                            points_on_current_line += 1
                max_points = max(max_points, points_on_current_line)
        # print(max_points)
        return max_points


assert Solution.maxPoints(points=[[1, 1], [2, 2], [3, 3]]) == 3
assert Solution.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
assert Solution.maxPoints(points=[[0, 0]]) == 1
assert Solution.maxPoints(
    [[54, 153], [1, 3], [0, -72], [-3, 3], [12, -22], [-60, -322], [0, -5], [-5, 1], [5, 5], [36, 78], [3, -4], [5, 0],
     [0, 4], [-30, -197], [-5, 0], [60, 178], [0, 0], [30, 53], [24, 28], [4, 5], [2, -2], [-18, -147], [-24, -172],
     [-36, -222], [-42, -247], [2, 3], [-12, -122], [-54, -297], [6, -47], [-5, 3], [-48, -272], [-4, -2], [3, -2],
     [0, 2], [48, 128], [4, 3], [2, 4]]) == 18
