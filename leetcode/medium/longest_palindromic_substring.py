"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:

    @staticmethod
    def longestPalindrome(s: str) -> str:
        return s


assert Solution.longestPalindrome("babad") == "bab"
# Note: "aba" is also a valid answer.
assert Solution.longestPalindrome("cbbd") == "bb"
assert Solution.longestPalindrome("a") == "a"
assert Solution.longestPalindrome("ac") == "a"
