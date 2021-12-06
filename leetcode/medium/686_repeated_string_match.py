"""
https://leetcode.com/problems/repeated-string-match/
"""


class Solution:
    @staticmethod
    def repeatedStringMatch(a: str, b: str) -> int:
        split_b = b.split(a)
        x = len(split_b) - 1
        if b in a * x:
            return x
        elif b in a * (x + 1):
            return x + 1
        elif b in a * (x + 2):
            return x + 2
        return -1


assert Solution.repeatedStringMatch(a="abcd", b="cdabcdab") == 3
"""
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
"""
assert Solution.repeatedStringMatch(a="a", b="aa") == 2
assert Solution.repeatedStringMatch(a="a", b="a") == 1
assert Solution.repeatedStringMatch(a="abc", b="wxyz") == -1
