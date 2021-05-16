"""
https://leetcode.com/contest/weekly-contest-241/problems/sum-of-all-subset-xor-totals/
"""

from itertools import combinations


class Solution:
    @staticmethod
    def subsets(nums):
        result = []
        length = len(nums)
        for size in range(1, length + 1):
            # print(list(combinations(nums, size)))
            result.append(list(combinations(nums, size)))
        return result

    def subsetXORSum(self, nums: [int]) -> int:
        xor = 0
        subsets = self.subsets(nums)
        for subset in subsets:
            # xor
            xe = 0
            for e in subset:
                x = 0
                for ei in e:
                    x ^= ei
                xe += x
            # print(x)
            xor += xe
        return xor


sol = Solution()
assert sol.subsetXORSum([1, 3]) == 6
assert sol.subsetXORSum([5, 1, 6]) == 28
assert sol.subsetXORSum([3, 4, 5, 6, 7, 8]) == 480
assert sol.subsetXORSum([2, 4, 4]) == 24
