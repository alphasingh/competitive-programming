"""
https://leetcode.com/problems/reordered-power-of-2/
"""

from itertools import permutations


class Solution:

    @staticmethod
    def isPowerOfTwo(x):
        return x and (not (x & (x - 1)))

    @staticmethod
    def reorderedPowerOf2(number: int) -> bool:
        string = str(number)  # string representation of number
        power_of_two_found = False
        for permutation in list(permutations(string)):
            if permutation[0] != '0' and Solution.isPowerOfTwo(int(''.join(permutation))):
                power_of_two_found = True
                break
        return power_of_two_found


assert Solution.reorderedPowerOf2(1) is True
assert Solution.reorderedPowerOf2(10) is False
assert Solution.reorderedPowerOf2(16) is True
assert Solution.reorderedPowerOf2(24) is False
assert Solution.reorderedPowerOf2(46) is True

"""
Example 1:
Input: 1
Output: true

Example 2:
Input: 10
Output: false

Example 3:
Input: 16
Output: true

Example 4:
Input: 24
Output: false

Example 5:
Input: 46
Output: true
"""
