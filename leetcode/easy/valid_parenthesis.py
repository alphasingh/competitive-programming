"""
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        return True


assert Solution.isValid("()") is True
assert Solution.isValid("()[]{}") is True
assert Solution.isValid("(]") is False
assert Solution.isValid("([)]") is False
assert Solution.isValid("{[]}") is True
