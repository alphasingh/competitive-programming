"""
https://leetcode.com/problems/arranging-coins/
"""

import math


class Solution:
    @staticmethod
    def arrangeCoins(n: int) -> int:
        c = -2 * n
        d = math.sqrt(1 - 4 * c)
        first = -1 + d
        second = -1 - d
        if first >= 0:
            x = first // 2
        else:
            x = second // 2
        return int(x)


assert Solution.arrangeCoins(5) == 2
assert Solution.arrangeCoins(8) == 3
assert Solution.arrangeCoins(2147483647) == 65535
assert Solution.arrangeCoins(2000000000) == 63245
