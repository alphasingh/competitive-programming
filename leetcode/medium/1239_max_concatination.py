"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
"""

from itertools import combinations


class Solution:
    @staticmethod
    def maxLength(arr: [str]) -> int:
        m = 0
        for size in range(len(arr) + 1):
            for combo in list(combinations(arr, size)):
                current = "".join(combo)
                word_len = len(current)
                if word_len == len(set(current)):
                    m = max(m, word_len)
        return m


assert Solution.maxLength(arr=["un", "iq", "ue"]) == 4
"""
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
"""
assert Solution.maxLength(arr=["cha", "r", "act", "ers"]) == 6
"""
Explanation: Possible solutions are "chaers" and "acters".
"""
assert Solution.maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]) == 26
assert Solution.maxLength(arr=["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"]) == 11
