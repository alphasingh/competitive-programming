"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:

    @staticmethod
    def longestPalindrome(s: str) -> str:
        max_length = 1
        longest_palindrome = s[0]
        length = len(s)
        is_palindrome = [[0 for _ in range(length)] for _ in range(length)]
        for start in range(length):
            is_palindrome[start][start] = 1  # single alphabet is palindrome
        for start in range(length - 1):
            if s[start] == s[start + 1]:  # is palindrome
                is_palindrome[start][start + 1] = 1
                if max_length < 2:
                    max_length = 2
                    longest_palindrome = s[start:start + 2]
        # print(is_palindrome)
        for size_of_substring in range(2, length):
            for start in range(length):
                end = start + size_of_substring
                if end < length:
                    if s[start] == s[end] and is_palindrome[start + 1][end - 1]:  # is palindrome
                        is_palindrome[start][end] = 1
                        if end - start + 1 > max_length:
                            max_length = end - start + 1
                            longest_palindrome = s[start:end + 1]
        # print(longest_palindrome, max_length)
        return longest_palindrome


assert Solution.longestPalindrome("eptcrhhlhrytwkytqmqlnvgoogjdlejnslpevrtxplzyzlvcy") == "lzyzl"
assert Solution.longestPalindrome("babad") == "bab"
# Note: "aba" is also a valid answer.
assert Solution.longestPalindrome("cbbd") == "bb"
assert Solution.longestPalindrome("a") == "a"
assert Solution.longestPalindrome("ac") == "a"
