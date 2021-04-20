"""
https://leetcode.com/problems/combination-sum-iv/
"""

from collections import Counter


class Solution:
    factorial = [1, 1, 2]

    def fact(self, number: int):
        if number > len(self.factorial) - 1:
            self.factorial.append(number * self.fact(number - 1))
        # print(number, self.factorial)
        return self.factorial[number]

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
        for unique in uniques:
            counter = Counter(unique)
            # print(counter)
            current_permutations = len(unique)
            # print("fact:", self.fact(current_permutations))
            numerator = self.fact(current_permutations)
            denominator = 1
            for key in counter:
                denominator *= self.fact(counter[key])
            # print('num:', numerator, 'den', denominator)
            permutations += numerator // denominator
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
