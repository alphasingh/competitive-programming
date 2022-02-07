"""
https://leetcode.com/problems/find-the-difference/
"""

from collections import Counter


class Solution:
    @staticmethod
    def findTheDifference(s: str, t: str) -> str:
        return list((Counter(t) - Counter(s)).keys())[0]


assert Solution.findTheDifference(s="abcd", t="abcde") == "e"
# Explanation: 'e' is the letter that was added.
assert Solution.findTheDifference(s="", t="y") == "y"
assert Solution.findTheDifference(s="y", t="yy") == "y"
