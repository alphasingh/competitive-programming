"""
https://leetcode.com/problems/find-common-characters/
"""

from collections import Counter


class Solution:
    @staticmethod
    def commonChars(words: [str]) -> [str]:
        common = dict(Counter(words[0]))
        for word in words:
            word_counter = Counter(word)
            for char in common:
                common[char] = min(word_counter[char], common[char])
        # print(common)
        common_alphabets = []
        for alphabet in common:
            common_alphabets += [alphabet] * common[alphabet]
        # print(common_alphabets)
        return common_alphabets


assert Solution.commonChars(words=["bella", "label", "roller"]) == ["e", "l", "l"]
assert Solution.commonChars(words=["cool", "lock", "cook"]) == ["c", "o"]
