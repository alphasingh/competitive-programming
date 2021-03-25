"""
https://leetcode.com/problems/advantage-shuffle/
"""


class Solution:

    @staticmethod
    def advantageCount(A: [int], B: [int]) -> [int]:
        return A + B


assert Solution.advantageCount(A=[2, 7, 11, 15], B=[1, 10, 4, 11]) == [2, 11, 7, 15]
assert Solution.advantageCount(A=[12, 24, 8, 32], B=[13, 25, 32, 11]) == [24, 32, 8, 12]
