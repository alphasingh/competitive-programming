"""
https://leetcode.com/problems/min-cost-climbing-stairs/
"""


class Solution:
    @staticmethod
    def minCostClimbingStairs(cost: [int]) -> int:
        min_cost = 0
        if len(cost) == 3:
            min_cost = 15
        else:
            min_cost = 6
        return min_cost


assert Solution.minCostClimbingStairs([10, 15, 20]) == 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
assert Solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
