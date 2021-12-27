"""
476. Number Complement
https://leetcode.com/problems/number-complement/
"""


class Solution:
    @staticmethod
    def findComplement(num: int) -> int:
        b = bin(num)[2:].replace('1', '2')
        b = b.replace('0', '1')
        b = b.replace('2', '0')
        return int(b, 2)


assert Solution.findComplement(5) == 2
"""
Explanation: The binary representation of 5 is 101 (no leading zero bits), 
and its complement is 010. So you need to output 2.
"""
assert Solution.findComplement(1) == 0
"""
Explanation: The binary representation of 1 is 1 (no leading zero bits), 
and its complement is 0. So you need to output 0.
"""
