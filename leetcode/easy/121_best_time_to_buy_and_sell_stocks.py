"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    @staticmethod
    def maxProfit(prices: [int]) -> int:
        max_profit = 0
        len_prices = len(prices)
        max_so_far = 0
        for i in range(len_prices - 1, -1, -1):
            max_so_far = max(max_so_far, prices[i])
            max_profit = max(max_profit, max_so_far - prices[i])
        return max_profit


assert Solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
"""
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed 
because you must buy before you sell.
"""
assert Solution.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
"""
Explanation: In this case, no transactions are done and the max profit = 0.
"""
