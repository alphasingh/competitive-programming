"""
https://leetcode.com/problems/interleaving-string/
"""


class Solution:

    @staticmethod
    def isInterleave(s1: str, s2: str, s3: str) -> bool:
        is_s3_possible = False
        return is_s3_possible


assert Solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") is True
assert Solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") is False
assert Solution.isInterleave(s1="", s2="", s3="") is True
