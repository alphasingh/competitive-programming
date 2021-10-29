"""
https://leetcode.com/problems/house-robber/
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for house in nums:
            rob = max(rob1 + house, rob2)
            rob1 = rob2
            rob2 = rob
        return rob2

      
sol = Solution()
assert sol.rob([1,2,3,1]) == 4
"""
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""
assert sol.rob([2,7,9,3,1]) == 12
"""
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
