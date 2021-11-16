"""
https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
"""


class Solution:
    @staticmethod
    def checkZeroOnes(s: str) -> bool:
        ones = [len(segment) for segment in s.split('0')]
        zeroes = [len(segment) for segment in s.split('1')]
        return max(ones) > max(zeroes)


assert Solution.checkZeroOnes("1101") is True
"""
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.
"""
assert Solution.checkZeroOnes("111000") is False
"""
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.
"""
assert Solution.checkZeroOnes("110100010") is False
"""
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.
"""
