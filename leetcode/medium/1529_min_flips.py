"""
https://leetcode.com/problems/minimum-suffix-flips/
"""


class Solution:
    @staticmethod
    def minFlips(target: str) -> int:
        n = len(target)
        c = '#'
        s = 0
        for i in range(n - 1, -1, -1):
            if target[i] != c:
                c = target[i]
                s += 1
        if target[0] == '0':
            s -= 1
        return s


assert Solution.minFlips(target="10111") == 3
"""
Explanation: Initially, s = "00000".
Choose index i = 2: "00000" -> "00111"
Choose index i = 0: "00111" -> "11000"
Choose index i = 1: "11000" -> "10111"
We need at least 3 flip operations to form target.
"""
assert Solution.minFlips(target="101") == 3
"""
Explanation: Initially, s = "000".
Choose index i = 0: "000" -> "111"
Choose index i = 1: "111" -> "100"
Choose index i = 2: "100" -> "101"
We need at least 3 flip operations to form target.
"""
assert Solution.minFlips(target="00000") == 0
"""
Explanation: We do not need any operations since the initial s already equals target.
"""
