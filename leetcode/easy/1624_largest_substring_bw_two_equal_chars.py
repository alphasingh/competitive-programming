"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""


class Solution:
    @staticmethod
    def maxLengthBetweenEqualCharacters(s: str) -> int:
        n = len(s)
        o = -2
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if s[j] == s[i]:
                    o = max(j - i - 1, o)
                    break
        return o


assert Solution.maxLengthBetweenEqualCharacters("aa") == 0
"""
Explanation: The optimal substring here is an empty substring between the two 'a's.
"""
assert Solution.maxLengthBetweenEqualCharacters("abca") == 2
"""
Explanation: The optimal substring here is "bc".
"""
assert Solution.maxLengthBetweenEqualCharacters("cbzxy") == -1
"""
Explanation: There are no characters that appear twice in s.
"""
assert Solution.maxLengthBetweenEqualCharacters("cabbac") == 4
"""
Explanation: The optimal substring here is "abba". 
Other non-optimal substrings include "bb" and "".
"""
