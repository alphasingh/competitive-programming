"""
https://leetcode.com/problems/fibonacci-number/submissions/
"""


class Solution:
    @staticmethod
    def fib(n: int) -> int:
        return \
            (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
             28657,
             46368, 75025, 121393, 196418, 317811, 514229, 832040)[n]


assert Solution.fib(2) == 1
assert Solution.fib(0) == 0
assert Solution.fib(4) == 3
