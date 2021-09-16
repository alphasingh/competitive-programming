"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""

from collections import Counter


class Solution:
    @staticmethod
    def firstUniqChar(s: str) -> int:
        freq = Counter(s)
        for index, character in enumerate(s):
            if freq[character] == 1:
                return index
        return -1


assert Solution.firstUniqChar("leetcode") == 0
assert Solution.firstUniqChar("loveleetcode") == 2
assert Solution.firstUniqChar("aabb") == -1
