"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""


class Solution:
    @staticmethod
    def kClosest(points: [[int]], k: int) -> [[int]]:
        p = len(points)
        for i in range(p):
            points[i] = [points[i][0] ** 2 + points[i][1] ** 2] + points[i]
        points.sort()
        return [point[1:] for point in points[:k]]


assert Solution.kClosest(points=[[1, 3], [-2, 2]], k=1) == [[-2, 2]]
"""
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
"""
assert Solution.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2) == [[3, 3], [-2, 4]]
"""
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""
assert Solution.kClosest([[1, 3], [-2, 2], [2, -2]], 2) == [[-2, 2], [2, -2]]
