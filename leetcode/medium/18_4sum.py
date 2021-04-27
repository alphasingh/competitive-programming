"""
https://leetcode.com/problems/4sum-ii/
"""

from itertools import product
from collections import Counter


class Solution:

    @staticmethod
    def fourSum(nums: [int], target: int) -> [[int]]:
        n, count = len(nums), 0
        combinations = []
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            combinations.append(tuple(sorted((nums[a], nums[b], nums[c], nums[d]))))
                            count += 1
        # print(count)
        # print(set(combinations))
        combinations = list(list(combo) for combo in set(combinations))
        # print(combinations)
        return combinations


assert sorted(Solution.fourSum(nums=[2, 2, 2, 2, 2], target=8)) == [[2, 2, 2, 2]]
assert sorted(Solution.fourSum([-5, 5, 4, -3, 0, 0, 4, -2], 4)) == [[-5, 0, 4, 5], [-3, -2, 4, 5]]
assert sorted(Solution.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
