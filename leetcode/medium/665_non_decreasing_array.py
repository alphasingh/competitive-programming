"""
https://leetcode.com/problems/non-decreasing-array/
"""


class Solution:
    @staticmethod
    def checkPossibility(nums: [int]) -> bool:
        nums = [-1e6] + nums + [1e6]
        possible = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if nums[i + 1] >= nums[i - 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                break
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                possible = False
                break
        # print(nums, possible)
        return possible


"""
[-1,4,2,3]
[2,3,1]
[4,2,1]
[1]
[1,1]
[1,2,3]
[3,3,3]
[9,-1,9]
[20,20,1,19,19]
"""
