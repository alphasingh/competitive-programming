"""
https://leetcode.com/problems/palindromic-substrings/
"""


class Solution:

    @staticmethod
    def isPalindrome(s: str) -> bool:
        return s == s[::-1]

    @staticmethod
    def countSubstrings(s: str) -> int:
        palindromes = 0
        length = len(s)
        for size in range(length):
            for start in range(length - size):
                substring = s[start:start + size + 1]
                if Solution.isPalindrome(substring):
                    palindromes += 1
        return palindromes


assert Solution.countSubstrings("abc") is 3
# Explanation: Three palindromic strings: "a", "b", "c".

assert Solution.countSubstrings("aaa") is 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
