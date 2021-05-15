"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    @staticmethod
    def maxSubArray(nums: [int]) -> int:
        c_sum = r_sum = 0
        for num in nums:
            r_sum += num
            if r_sum > c_sum:
                c_sum = r_sum
            else:
                if r_sum < 0:
                    r_sum = 0
        if c_sum == 0:
            c_sum = max(nums)
        return c_sum


assert Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
assert Solution.maxSubArray([1]) == 1
assert Solution.maxSubArray([5, 4, -1, 7, 8]) == 23
assert Solution.maxSubArray([-2]) == -2
assert Solution.maxSubArray([-1, 0]) == 0
