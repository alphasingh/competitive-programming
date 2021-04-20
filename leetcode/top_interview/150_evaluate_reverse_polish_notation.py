"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


class Solution:

    def evalRPN(self, tokens: [str]) -> int:
        evaluation = len(tokens)
        return evaluation


sol = Solution()

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
