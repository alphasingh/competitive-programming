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
                for point in points:
                    if (point[1] - line_end[1]) * x_diff == (point[0] - line_end[0]) * y_diff:
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
assert Solution.maxPoints(
    [[4, -3], [970, 680], [-97, -35], [3, 8], [60, 253], [0, -13], [-270, -748], [-291, -165], [270, 890], [90, 228],
     [-220, -270], [-255, -118], [873, 615], [-42, -175], [440, 345], [4, -9], [170, 27], [425, 114], [56, 203],
     [531, 872], [295, 480], [231, 193], [291, 225], [680, 201], [-10, 9], [-388, -230], [-385, -127], [-590, -990],
     [-7, -40], [308, 222], [-616, -247], [-70, -283], [150, 526], [77, 113], [396, 304], [-264, -311], [-6, -8],
     [-88, -147], [30, 162], [49, 176], [81, 196], [-9, -124], [-27, -188], [-14, -67], [308, 233], [413, 676],
     [-77, 33], [-177, -304], [0, -31], [472, 774], [462, 313], [-35, -148], [1, -2], [-440, -475], [154, 153],
     [485, 355], [-231, -47], [340, 85], [-60, -111], [42, 149], [-354, -598], [388, 290], [44, -24], [3, -8],
     [510, 143], [-308, -352], [-18, -156], [-21, -94], [-63, -316], [-118, -206], [0, 73], [-240, -657], [-352, -393],
     [-531, -892], [-485, -295], [352, 263], [616, 393], [-154, -7], [3, 4], [-5, -9], [63, 230], [385, 273],
     [-679, -425], [-595, -234], [-582, -360], [-176, -229], [770, 473], [-539, -207], [-56, -229], [-236, -402],
     [-970, -620], [-425, -176], [240, 799], [118, 186], [10, -7], [-680, -263], [-5, 7], [220, 140], [-2, 7],
     [-28, -121], [-300, -839], [-54, -284], [-194, -100], [-308, -87], [-3, -10], [-873, -555], [-90, -202],
     [-5, -4]]) == 16
