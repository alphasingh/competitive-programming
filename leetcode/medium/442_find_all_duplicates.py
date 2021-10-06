"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""

from collections import Counter


class Solution:
    @staticmethod
    def findDuplicates(nums: [int]) -> [int]:
        f = Counter(nums)
        for t in f:
            if f[t] == 2:
                yield t


assert set(Solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) == {2, 3}
assert set(Solution.findDuplicates([1, 1, 2])) == {1}
assert set(Solution.findDuplicates([1])) == set()
