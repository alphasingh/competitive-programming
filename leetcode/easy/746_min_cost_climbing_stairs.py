"""
https://leetcode.com/problems/min-cost-climbing-stairs/
"""


class Solution:
    @staticmethod
    def minCostClimbingStairs(cost: [int]) -> int:
        n = len(cost)
        first = cost[0]
        second = cost[1]
        for i in range(2, n):
            current = cost[i] + min(first, second)
            first = second
            second = current
        return min(first, second)


assert Solution.minCostClimbingStairs([10, 15, 20]) == 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
assert Solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
