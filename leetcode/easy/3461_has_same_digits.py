"""
https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i
3461. Check If Digits Are Equal in String After Operations I
"""


class Solution:
    @staticmethod
    def hasSameDigits(s: str) -> bool:

        def operation(si):
            nsi = ""
            for i in range(len(si) - 1):
                nsi += str((int(s[i]) + int(s[i + 1])) % 10)
            return nsi

        while len(s) > 2:
            s = operation(s)

        # print(s)
        return s[0] == s[1]


assert Solution.hasSameDigits("3902") is True
assert Solution.hasSameDigits("34789") == False
