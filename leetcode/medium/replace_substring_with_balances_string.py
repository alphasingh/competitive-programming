"""
https://leetcode.com/problems/replace-the-substring-for-balanced-string/
"""


class Solution:

    @staticmethod
    def balancedString(s: str) -> int:
        return len(s)


assert Solution.balancedString(s="QWER") is 0
# Explanation: s is already balanced.
assert Solution.balancedString(s="QQWE") is 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
assert Solution.balancedString(s="QQQW") is 2
# Explanation: We can replace the first "QQ" to "ER".
assert Solution.balancedString(s="QQQQ") is 3
# Explanation: We can replace the last 3 'Q' to make s = "QWER".
