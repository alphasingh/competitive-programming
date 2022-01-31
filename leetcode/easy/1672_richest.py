"""
https://leetcode.com/problems/richest-customer-wealth/
"""


class Solution:
    @staticmethod
    def maximumWealth(accounts: [[int]]) -> int:
        return max(sum(money) for money in accounts)


assert Solution.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]) == 6
"""
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
"""
assert Solution.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]) == 10
"""
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
"""
assert Solution.maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
