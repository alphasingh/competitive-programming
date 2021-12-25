"""
https://leetcode.com/problems/basic-calculator-ii/
"""


class Solution:
    @staticmethod
    def calculate(s: str) -> int:
        stack = []
        operator = '+'
        current_number = ''
        for i in range(len(s)):
            ch = s[i]
            if '0' <= ch <= '9':
                current_number += ch
            if (not '0' <= ch <= '9' and ch != ' ') or (i == len(s) - 1):
                if operator == '+':
                    stack.append(int(current_number))
                elif operator == '-':
                    stack.append(-int(current_number))
                elif operator == '*':
                    stack.append(stack.pop() * int(current_number))
                elif operator == '/':
                    stack.append(int(stack.pop() / int(current_number)))
                operator = ch
                current_number = ''
            # print(stack)
        # print(stack, current_number)
        return sum(stack)


assert Solution.calculate(" 3+5 / 2 ") == 5
assert Solution.calculate(" 394   +2 + 2 ") == 398
assert Solution.calculate("3+2*2") == 7
assert Solution.calculate(" 3/2 ") == 1
