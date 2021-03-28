"""
https://leetcode.com/problems/palindromic-substrings/
"""


class Solution:

    @staticmethod
    def countSubstrings(s: str) -> int:
        return len(s)


assert Solution.countSubstrings("abc") is 3
# Explanation: Three palindromic strings: "a", "b", "c".

assert Solution.countSubstrings("aaa") is 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
