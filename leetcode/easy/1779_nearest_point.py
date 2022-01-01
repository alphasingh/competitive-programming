"""
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
"""


class Solution:
    @staticmethod
    def nearestValidPoint(x: int, y: int, points: [[int]]) -> int:
        i = -1
        d = 1_000_000
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                md = abs(point[0] - x) + abs(point[1] - y)
                if md < d:
                    d = md
                    i = index
        return i


assert Solution.nearestValidPoint(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]) == 2
"""
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. 
Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, 
with a distance of 1. [2,4] has the smallest index, so return 2.
"""
assert Solution.nearestValidPoint(x=3, y=4, points=[[3, 4]]) == 0
"""
Explanation: The answer is allowed to be on the same location as your current location.
"""
assert Solution.nearestValidPoint(x=3, y=4, points=[[2, 3]]) == -1
"""
Explanation: There are no valid points.
"""
