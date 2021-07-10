"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""


class Solution:
    @staticmethod
    def lengthOfLIS(nums: [int]) -> int:
        nums_length = len(nums)
        dp = [1] * nums_length
        for j in range(nums_length):
            for i in range(j):
                if nums[i] < nums[j]:
                    curr = dp[i] + 1
                else:
                    curr = dp[j]
                dp[j] = max(dp[j], curr)
        return max(dp)


assert Solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4
"""
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""
assert Solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4
assert Solution.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]) == 1
assert Solution.lengthOfLIS([100, 9, 2, 9, 3, 7, 101, 6]) == 4
