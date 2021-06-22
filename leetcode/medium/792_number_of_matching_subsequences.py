"""
https://leetcode.com/problems/number-of-matching-subsequences/
"""


class Solution:
    @staticmethod
    def numMatchingSubseq(s: str, words: [str]) -> int:
        matches = 0
        return matches


assert Solution.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]) == 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

assert Solution.numMatchingSubseq(s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]) == 2
