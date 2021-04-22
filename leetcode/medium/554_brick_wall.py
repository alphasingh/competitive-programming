"""
https://leetcode.com/problems/brick-wall/
"""


class Solution:

    def leastBricks(self, wall: [[int]]) -> int:
        brick_edge_frequency = dict()
        for row_of_bricks in wall:
            brick_edge = 0  # brick row start from 0
            for brick in row_of_bricks[:-1]:  # exclude last brick
                brick_edge += brick
                brick_edge_frequency.setdefault(brick_edge, 0)
                brick_edge_frequency[brick_edge] += 1
        # print(brick_edge_frequency)
        most_frequent_brick_edge = max(brick_edge_frequency.values()) if brick_edge_frequency.values() else 0
        return len(wall) - most_frequent_brick_edge


sol = Solution()
assert sol.leastBricks([[1, 2, 2, 1],
                        [3, 1, 2],
                        [1, 3, 2],
                        [2, 4],
                        [3, 1, 2],
                        [1, 3, 1, 1]]) == 2

assert sol.leastBricks([[1], [1], [1]]) == 3
