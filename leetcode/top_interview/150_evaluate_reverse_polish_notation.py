"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


class Solution:

    @staticmethod
    def perform_operation(a: int, b: int, operator: str) -> int:
        result = 0
        if operator == '+':
            result = a + b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            # print('division', a, b, a // b)
            # print('division', abs(a), abs(b), a // b)
            result = a // b
            if (abs(a) // b) == 0 or (a // abs(b)) == 0:
                result = 0
        elif operator == '-':
            result = a - b
        return result

    @staticmethod
    def is_token_operator(token: str) -> bool:
        return token in ('+', '-', '*', '/')

    def evalRPN(self, tokens: [str]) -> int:
        evaluation = 0
        stack = []
        for token in tokens:
            # print(stack)
            if self.is_token_operator(token):
                last = int(stack.pop())
                second_last = int(stack.pop())
                result = self.perform_operation(second_last, last, token)
                stack.append(str(result))
            else:
                stack.append(token)
        # print(stack)
        evaluation = int(stack.pop())
        return evaluation


sol = Solution()

assert sol.evalRPN(tokens=["2", "1", "+", "4", "-"]) == -1
# Explanation: ((2 + 1) - 4) = -1

assert sol.evalRPN(tokens=["2", "1", "+", "3", "*"]) == 9
# Explanation: ((2 + 1) * 3) = 9

assert sol.evalRPN(tokens=["4", "13", "5", "/", "+"]) == 6
# Explanation: (4 + (13 / 5)) = 6

assert sol.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
"""
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
