"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:

    @staticmethod
    def longestPalindrome(s: str) -> str:
        max_length = 0
        longest_palindrome = ""
        length = len(s)
        for start in range(length):
            for end in range(start + 1, length + 1):
                substring = s[start:end]
                if substring == substring[::-1] and end - start > max_length:  # is palindrome
                    max_length = end - start
                    longest_palindrome = substring
        return longest_palindrome


assert Solution.longestPalindrome("babad") == "bab"
# Note: "aba" is also a valid answer.
assert Solution.longestPalindrome("cbbd") == "bb"
assert Solution.longestPalindrome("a") == "a"
assert Solution.longestPalindrome("ac") == "a"
