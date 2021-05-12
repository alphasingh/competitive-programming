"""
https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        sign = 1 if x >= 0 else -1
        reversed_integer = sign * int(str(abs(x))[::-1])
        return [0, reversed_integer][-2147483647 <= reversed_integer <= 2147483647]


assert Solution.reverse(123) == 321
assert Solution.reverse(1534236469) == 0
assert Solution.reverse(-2147483647) == 0
assert Solution.reverse(-1534236469) == 0
assert Solution.reverse(-123) == -321
assert Solution.reverse(120) == 21
assert Solution.reverse(0) == 0
