"""
https://leetcode.com/problems/ransom-note/
"""

from collections import Counter


class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        for key in rc:
            if (key not in mc) or (mc[key] < rc[key]):
                return False
        return True


assert Solution.canConstruct(ransomNote="a", magazine="b") is False
assert Solution.canConstruct(ransomNote="aa", magazine="ab") is False
assert Solution.canConstruct(ransomNote="aa", magazine="aab") is True
