"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""


class Solution:
    @staticmethod
    def maxProfit(prices: [int]) -> int:
        cache = {}
        n = len(prices)

        def dfs(i, buying):
            if i >= n:
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]

            if buying:
                total = dfs(i + 1, False) - prices[i]
            else:
                total = dfs(i + 2, True) + prices[i]

            total = max(total, dfs(i + 1, buying))

            cache[(i, buying)] = total
            return cache[(i, buying)]

        return dfs(0, True)


assert Solution.maxProfit(prices=[1, 2, 3, 0, 2]) == 3
assert Solution.maxProfit(prices=[1]) == 0
