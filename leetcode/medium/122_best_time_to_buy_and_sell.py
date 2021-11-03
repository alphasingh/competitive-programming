"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


class Solution:
    @staticmethod
    def maxProfit(prices: [int]) -> int:
        stock_price = 0
        profit = 0
        days = len(prices)
        for day in range(days - 1, -1, -1):
            if prices[day] < stock_price:
                profit += stock_price - prices[day]
                stock_price = prices[day]
            else:
                stock_price = max(stock_price, prices[day])
        return profit


assert Solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 7
"""
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""
assert Solution.maxProfit(prices=[1, 2, 3, 4, 5]) == 4
"""
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
"""
assert Solution.maxProfit(prices=[7, 6, 4, 3, 1]) == 0
"""
Explanation: There is no way to make a positive profit, 
so we never buy the stock to achieve the maximum profit of 0.
"""
