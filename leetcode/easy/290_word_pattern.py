"""
https://leetcode.com/problems/word-pattern/
"""


class Solution:
    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        words_list = s.split()
        len_pattern = len(pattern)
        len_words = len(words_list)
        if len_pattern != len_words:
            return False
        mapping = dict()
        for i in range(len_words):  # len_words == len_pattern
            if pattern[i] not in mapping:
                mapping[pattern[i]] = words_list[i]
            if mapping[pattern[i]] != words_list[i]:
                return False
        return len(mapping) == len(set(mapping.values()))


assert Solution.wordPattern(pattern="abba", s="dog cat cat dog") is True
assert Solution.wordPattern(pattern="abba", s="dog cat cat fish") is False
assert Solution.wordPattern(pattern="aaaa", s="dog cat cat dog") is False
assert Solution.wordPattern(pattern="abba", s="dog dog dog dog") is False
