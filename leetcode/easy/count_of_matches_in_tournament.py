"""
https://leetcode.com/problems/count-of-matches-in-tournament/
"""


class Solution:
    @staticmethod
    def numberOfMatches(n: int) -> int:
        m = 0
        while n != 1:
            m += n // 2
            if n & 1:  # n is odd
                n = n // 2 + 1
            else:  # n is even
                n = n // 2
        # print(m)
        return m


assert Solution.numberOfMatches(7) is 6

assert Solution.numberOfMatches(14) is 13
