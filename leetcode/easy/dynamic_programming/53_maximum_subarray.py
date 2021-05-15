"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    @staticmethod
    def maxSubArray(nums: [int]) -> int:
        max_sum = nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
            max_sum = max(nums[i], max_sum)
        return max_sum


assert Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
assert Solution.maxSubArray([1]) == 1
assert Solution.maxSubArray([5, 4, -1, 7, 8]) == 23
assert Solution.maxSubArray([-2]) == -2
assert Solution.maxSubArray([-1, 0]) == 0
