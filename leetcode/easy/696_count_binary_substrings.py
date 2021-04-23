"""
https://leetcode.com/problems/count-binary-substrings/
"""


class Solution:
    @staticmethod
    def countBinarySubstrings(s: str) -> int:
        count = len(s)
        return count


assert Solution.countBinarySubstrings("00110011") == 6
"""
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: 
"0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
"""
assert Solution.countBinarySubstrings("10101") == 4
"""
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
"""

assert Solution.countBinarySubstrings("000111") == 3
assert Solution.countBinarySubstrings("11100") == 2
assert Solution.countBinarySubstrings("00011100") == 5
