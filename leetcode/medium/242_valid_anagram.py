"""
https://leetcode.com/problems/valid-anagram/
"""

from collections import Counter


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


assert Solution.isAnagram(s="anagram", t="nagaram") is True
assert Solution.isAnagram(s="rat", t="car") is False
