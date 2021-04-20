"""
https://leetcode.com/problems/combination-sum/
"""


class Solution:

    def dfs(self, nums: [int], start: int, target: int, path: [int], result: [[int]]):
        if target < 0:
            return
        elif target == 0:
            result.append(path)
            return
        for search in range(start, len(nums)):
            self.dfs(nums, search, target - nums[search], path + [nums[search]], result)

    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        result = []
        self.dfs(candidates, 0, target, [], result)
        # print(result)
        return result


sol = Solution()

assert sol.combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
assert sol.combinationSum(candidates=[2, 3, 5], target=8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
assert sol.combinationSum(candidates=[1], target=2) == [[1, 1]]
assert sol.combinationSum(candidates=[2], target=1) == []
assert sol.combinationSum(candidates=[1], target=1) == [[1]]
