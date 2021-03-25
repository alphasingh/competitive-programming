"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
"""


class Solution:
    @staticmethod
    def maxDepth(s: str) -> int:
        current_depth = max_depth = 0
        for character in s:
            if character == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif character == ')':
                current_depth -= 1
        return max_depth


assert Solution.maxDepth(s="(1+(2*3)+((8)/4))+1") is 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string
assert Solution.maxDepth(s="(1)+((2))+(((3)))") is 3
assert Solution.maxDepth(s="1+(2*3)/(2-1)") is 1
assert Solution.maxDepth(s="1") is 0
