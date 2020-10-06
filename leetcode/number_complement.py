"""
476. Number Complement
https://leetcode.com/problems/number-complement/
"""


class Solution:
    @staticmethod
    def findComplement(num: int) -> int:
        number_in_binary = bin(num)
        all_bits_set_in_binary = '1' * (len(number_in_binary) - 2)
        set_number_in_decimal = int(all_bits_set_in_binary, 2)
        return set_number_in_decimal - num


print(Solution.findComplement(num=5))
print(Solution.findComplement(num=1))

"""
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""
