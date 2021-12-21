"""
https://leetcode.com/problems/power-of-two/
"""


class Solution:
    @staticmethod
    def isPowerOfTwo(n: int) -> bool:
        return bin(n).strip('0') == 'b1'


assert Solution.isPowerOfTwo(1) is True
# Explanation: 2**0 = 1
assert Solution.isPowerOfTwo(16) is True
# Explanation: 2**4 = 16
assert Solution.isPowerOfTwo(3) is False
assert Solution.isPowerOfTwo(6) is False
