"""
https://leetcode.com/problems/power-of-three/
"""


class Solution:
    POWERS = (1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721,
              129140163, 387420489, 1162261467)

    @staticmethod
    def isPowerOfThree(n: int) -> bool:
        return n in Solution.POWERS


assert Solution.isPowerOfThree(27) is True
assert Solution.isPowerOfThree(0) is False
assert Solution.isPowerOfThree(45) is False
assert Solution.isPowerOfThree(9) is True
assert Solution.isPowerOfThree(-9) is False
