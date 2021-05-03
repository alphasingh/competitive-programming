"""
https://leetcode.com/problems/running-sum-of-1d-array/
"""


class Solution:
    @staticmethod
    def runningSum(nums: [int]) -> [int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


assert Solution.runningSum(nums=[1, 2, 3, 4]) == [1, 3, 6, 10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

assert Solution.runningSum(nums=[1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

assert Solution.runningSum(nums=[3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
