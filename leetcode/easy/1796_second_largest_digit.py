"""
https://leetcode.com/problems/second-largest-digit-in-a-string/
"""


class Solution:
    @staticmethod
    def secondHighest(s: str) -> int:
        digits = set()
        for char in s:
            if '0' <= char <= '9':
                digits.add(char)
        digits = list(digits)
        digits.sort(reverse=True)
        # print(digits)
        if len(digits) > 1:
            return int(digits[1])
        return -1


assert Solution.secondHighest("dfa12321afd") == 2
assert Solution.secondHighest("abc1111") == -1
assert Solution.secondHighest("ck077") == 0
