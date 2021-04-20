"""
https://leetcode.com/problems/find-the-duplicate-number/
"""


class Solution:

    def findDuplicate(self, nums: [int]) -> int:
        n = len(nums) - 1
        sum_of_n_numbers = n * (n + 1) // 2
        return sum(nums) - sum_of_n_numbers


sol = Solution()

assert sol.findDuplicate(nums=[1, 3, 4, 2, 2]) == 2
assert sol.findDuplicate(nums=[3, 1, 3, 4, 2]) == 3
assert sol.findDuplicate(nums=[1, 1]) == 1
assert sol.findDuplicate(nums=[1, 1, 2]) == 1
assert sol.findDuplicate(nums=[1, 3, 3]) == 3
