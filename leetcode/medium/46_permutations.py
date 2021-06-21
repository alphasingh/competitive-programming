"""
https://leetcode.com/problems/permutations/
"""

from itertools import permutations


class Solution:

    @staticmethod
    def permute(nums: [int]) -> [[int]]:
        nums_permutations = list(permutations(nums))
        # print(nums_permutations)
        return nums_permutations


assert Solution.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
assert Solution.permute([0, 1]) == [[0, 1], [1, 0]]
assert Solution.permute([1]) == [[1]]
