"""
https://leetcode.com/problems/find-the-duplicate-number/
"""


class Solution:

    @staticmethod
    def findDuplicate(nums: [int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return 1


sol = Solution()

assert sol.findDuplicate(nums=[1, 3, 4, 2, 2]) == 2
assert sol.findDuplicate(nums=[3, 1, 3, 4, 2]) == 3
assert sol.findDuplicate(nums=[1, 1]) == 1
assert sol.findDuplicate(nums=[1, 1, 2]) == 1
assert sol.findDuplicate(nums=[2, 2, 2]) == 2
assert sol.findDuplicate(nums=[1, 3, 4, 4, 4]) == 4
