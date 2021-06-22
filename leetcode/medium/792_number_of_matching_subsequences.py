"""
https://leetcode.com/problems/number-of-matching-subsequences/
"""

from functools import lru_cache


class Solution:
    @lru_cache()
    def subsequence_exists(self, word: str, string: str) -> bool:
        pointer = 0
        pointer_limit = len(word)
        for char in string:
            if char == word[pointer]:
                pointer += 1
            if pointer >= pointer_limit:
                break
        return pointer_limit == pointer

    def numMatchingSubseq(self, s: str, words: [str]) -> int:
        matches = 0
        for word in words:
            if self.subsequence_exists(word, s):
                matches += 1
        return matches


solution = Solution()
assert solution.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]) == 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

assert solution.numMatchingSubseq(s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]) == 2
