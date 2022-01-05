"""
https://leetcode.com/problems/valid-palindrome-ii/
"""


class Solution:
    @staticmethod
    def validPalindrome(s: str) -> bool:
        d = 0
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                d += 1
                left -= 1
            left += 1
            right -= 1
        if d < 2:
            return True
        d = 0
        left = 0
        s = s[::-1]
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                d += 1
                left -= 1
            left += 1
            right -= 1
        return d < 2


assert Solution.validPalindrome("aba") is True
assert Solution.validPalindrome("abca") is True
assert Solution.validPalindrome("abc") is False
