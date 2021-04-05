"""
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        stack = []
        valid_stack = True
        for bracket in s:
            if bracket == "(":
                stack.append(bracket)
            elif bracket == "[":
                stack.append(bracket)
            elif bracket == "{":
                stack.append(bracket)
            elif bracket == ")":
                valid_stack = True if stack and stack.pop() == "(" else False
            elif bracket == "]":
                valid_stack = True if stack and stack.pop() == "[" else False
            elif bracket == "}":
                valid_stack = True if stack and stack.pop() == "{" else False
            if not valid_stack:
                break
        return len(stack) == 0 and valid_stack


assert Solution.isValid("()") is True
assert Solution.isValid("()[]{}") is True
assert Solution.isValid("(]") is False
assert Solution.isValid("([)]") is False
assert Solution.isValid("{[]}") is True
assert Solution.isValid("[") is False
assert Solution.isValid("({{{{}}}))") is False
