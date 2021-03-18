"""
https://leetcode.com/problems/generate-random-point-in-a-circle/
https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly
"""

import math
import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    @staticmethod
    def random_0_to_1() -> float:
        return random.random()  # Random float:  0.0 <= x < 1.0

    def randPoint(self) -> [float]:
        r = self.radius * math.sqrt(Solution.random_0_to_1())
        theta = Solution.random_0_to_1() * 2 * math.pi
        random_x = self.x_center + r * math.cos(theta)
        random_y = self.y_center + r * math.sin(theta)
        return [random_x, random_y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

"""
Example 1:
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
"""
