"""
https://leetcode.com/problems/power-of-three/
"""


class Solution:

    @staticmethod
    def isPowerOfThree(n: int) -> bool:
        return n > 0 and 1162261467 % n == 0  # divides 3**19


assert Solution.isPowerOfThree(27) is True
assert Solution.isPowerOfThree(0) is False
assert Solution.isPowerOfThree(45) is False
assert Solution.isPowerOfThree(9) is True
assert Solution.isPowerOfThree(-9) is False
