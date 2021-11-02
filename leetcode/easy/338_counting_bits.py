"""
https://leetcode.com/problems/counting-bits/
"""


class Solution:
    @staticmethod
    def countBits(n: int) -> [int]:
        return [bin(i).count('1') for i in range(n + 1)]


assert Solution.countBits(2) == [0, 1, 1]
assert Solution.countBits(5) == [0, 1, 1, 2, 1, 2]
"""
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""
