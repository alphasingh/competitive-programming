"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
"""


class Solution:
    @staticmethod
    def maxDepth(s: str) -> int:
        return len(s)


assert Solution.maxDepth(s="(1+(2*3)+((8)/4))+1") is 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string
assert Solution.maxDepth(s="(1)+((2))+(((3)))") is 3
assert Solution.maxDepth(s="1+(2*3)/(2-1)") is 1
assert Solution.maxDepth(s="1") is 0
