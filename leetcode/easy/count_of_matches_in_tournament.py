"""
https://leetcode.com/problems/count-of-matches-in-tournament/
"""


class Solution:
    @staticmethod
    def numberOfMatches(n: int) -> int:
        return n - 1


assert Solution.numberOfMatches(7) is 6

assert Solution.numberOfMatches(14) is 13
