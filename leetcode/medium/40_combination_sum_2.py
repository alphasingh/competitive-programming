"""
https://leetcode.com/problems/combination-sum-ii/
"""


class Solution:

    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        print(self, target)
        return candidates


sol = Solution()

assert sol.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8) == [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6]
]
assert sol.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5) == [
    [1, 2, 2],
    [5]
]
