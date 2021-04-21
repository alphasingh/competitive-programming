"""
https://leetcode.com/problems/basic-calculator-ii/
"""


class Solution:

    @staticmethod
    def calculate(s: str) -> int:
        result = 0
        expression = []
        number = ""  # initialize number
        for token in "".join(s.split()):
            if token in "+-*/":  # operator
                if number != "":  # add number if any before adding next operator
                    expression.append(int(number))
                    number = ""  # reinitialize number
                expression.append(token)
            elif token in "01234567890":
                number += token
        if number != "":  # last number if any
            expression.append(int(number))
        print(expression)
        pointer = 0
        expression_length = len(expression)
        # solve all divisions
        while pointer < expression_length - 2:
            if expression[pointer + 1] == '/':  # triplet with division found
                expression[pointer] = int(expression[pointer] / expression[pointer + 2])
                expression[pointer + 1] = '-'
                expression[pointer + 2] = 0
                expression_length -= 2
            else:
                pointer += 1
        # solve all multiplications
        # solve all additions
        # solve all subtractions
        print(expression)
        return result


assert Solution.calculate(" 3+5 / 2 ") == 5
assert Solution.calculate(" 394   +2 + 2 ") == 398
assert Solution.calculate("3+2*2") == 7
assert Solution.calculate(" 3/2 ") == 1
