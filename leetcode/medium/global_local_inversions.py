"""
https://leetcode.com/problems/global-and-local-inversions/
"""


class Solution:

    @staticmethod
    def isIdealPermutation(A: [int]) -> bool:
        return len(A) ^ 1 == 0


assert Solution.isIdealPermutation(A=[1, 0, 2]) is True
# Explanation: There is 1 global inversion, and 1 local inversion.
assert Solution.isIdealPermutation(A=[1, 2, 0]) is True
# Explanation: There are 2 global inversions, and 1 local inversion.
