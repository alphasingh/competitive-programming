"""
https://leetcode.com/problems/beautiful-arrangement-ii/
"""


class Solution:
    @staticmethod
    def constructArray(n: int, k: int) -> [int]:
        return [k] * n


assert Solution.constructArray(n=3, k=1) == [1, 2, 3]
"""
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, 
and the [1, 1] has exactly 1 distinct integer: 1.
"""
assert Solution.constructArray(n=3, k=2) == [1, 3, 2]
"""
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, 
and the [2, 1] has exactly 2 distinct integers: 1 and 2.
"""
