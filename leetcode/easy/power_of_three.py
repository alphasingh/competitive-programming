"""
https://leetcode.com/problems/power-of-three/
"""


class Solution:
    POWERS = [3 ** i for i in range(20)]

    @staticmethod
    def isPowerOfThree(n: int) -> bool:
        return n in Solution.POWERS


assert Solution.isPowerOfThree(27) is True
assert Solution.isPowerOfThree(0) is False
assert Solution.isPowerOfThree(45) is False
assert Solution.isPowerOfThree(9) is True
assert Solution.isPowerOfThree(-9) is False
