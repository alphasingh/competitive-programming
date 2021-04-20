"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


class Solution:

    def evalRPN(self, tokens: [str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                right, left = int(stack.pop()), int(stack.pop())
                if token == '+':
                    result = left + right
                elif token == '*':
                    result = left * right
                elif token == '/':
                    result = int(float(left) / right)
                else:
                    result = left - right
                stack.append(str(result))
            else:
                stack.append(token)
        return int(stack.pop())


sol = Solution()

failing_tokens = ["-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-",
                  "16", "/", "26", "-14", "-", "-", "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+",
                  "120", "*", "-60", "+", "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44", "*", "180",
                  "70", "-40", "-", "*", "86", "132", "-84", "+", "*", "-", "38", "/", "/", "21", "28", "/", "+", "83",
                  "/", "-31", "156", "-", "+", "28", "/", "95", "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73",
                  "/", "-62", "/", "93", "*", "196", "-", "-59", "+", "187", "-", "143", "/", "-79", "-89", "+", "-"]
assert sol.evalRPN(failing_tokens) == 165

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
