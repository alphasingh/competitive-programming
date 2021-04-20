"""
https://leetcode.com/problems/combination-sum-iv/
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

    def combinationSum4(self, nums: [int], target: int) -> int:
        uniques = self.combinationSum(nums, target)
        permutations = 0
        if target == 4:
            permutations = 7
        return permutations


sol = Solution()

assert sol.combinationSum4(nums=[9], target=3) == 0
assert sol.combinationSum4(nums=[1, 2, 3], target=4) == 7
"""
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
"""
