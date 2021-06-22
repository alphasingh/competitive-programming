"""
https://leetcode.com/problems/number-of-matching-subsequences/
"""


class Solution:
    @staticmethod
    def subsequence_exists(word: str, string: str):
        pointer = 0
        pointer_limit = len(word)
        for char in string:
            if char == word[pointer]:
                pointer += 1
            if pointer >= pointer_limit:
                break
        return pointer_limit == pointer

    @staticmethod
    def numMatchingSubseq(s: str, words: [str]) -> int:
        matches = 0
        for word in words:
            if Solution.subsequence_exists(word, s):
                matches += 1
        return matches


assert Solution.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]) == 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

assert Solution.numMatchingSubseq(s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]) == 2
