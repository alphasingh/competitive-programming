"""
https://leetcode.com/problems/score-of-parentheses/
"""


class Solution:
    @staticmethod
    def score_of_parentheses(s: str) -> int:
        stack = []
        for bracket in s:
            if bracket == '(':
                stack.append(bracket)
            else:
                # "()" has score 1
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0
                    while stack[-1] != '(':
                        # (A) has score 2 * A
                        score += stack.pop()
                    stack.pop()
                    stack.append(score * 2)
        # print(stack)
        return sum(stack)


assert Solution.score_of_parentheses("()") == 1
assert Solution.score_of_parentheses("(())") == 2
assert Solution.score_of_parentheses("()()") == 2
assert Solution.score_of_parentheses("(()()())") == 6
assert Solution.score_of_parentheses("((())()())") == 8
assert Solution.score_of_parentheses("((()()))()((()()))()") == 18
