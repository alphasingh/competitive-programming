"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""


class Solution:
    OPEN = '('
    CLOSE = ')'

    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for bracket in s:
            if bracket == self.OPEN:
                stack.append(self.OPEN)
            else:
                if stack and stack[-1] == self.OPEN:
                    stack.pop()
                else:
                    stack.append(self.CLOSE)
        # print(stack)
        return len(stack)


sol = Solution()
assert sol.minAddToMakeValid("())") == 1
assert sol.minAddToMakeValid("(((") == 3
