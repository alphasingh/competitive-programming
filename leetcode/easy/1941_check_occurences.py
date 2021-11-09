"""
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
"""
from collections import Counter


class Solution:
    @staticmethod
    def areOccurrencesEqual(s: str) -> bool:
        return len(set(Counter(s).values())) == 1


assert Solution.areOccurrencesEqual("abacbc") is True
"""
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
"""
assert Solution.areOccurrencesEqual("aaabb") is False
"""
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
"""
