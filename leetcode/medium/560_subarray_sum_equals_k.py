"""
https://leetcode.com/problems/subarray-sum-equals-k/
"""


class Solution:
    @staticmethod
    def subarraySum(nums: [int], k: int) -> int:
        n = len(nums)
        sums = {0: 1}
        running_sum = 0
        count = 0
        for i in range(n):
            running_sum += nums[i]
            left = running_sum - k
            if left in sums:
                count += sums[left]
            if running_sum not in sums:
                sums[running_sum] = 0
            sums[running_sum] += 1
        # print(sums)
        return count


assert Solution.subarraySum(nums=[1, 1, 1], k=2) == 2
assert Solution.subarraySum(nums=[1, 2, 3], k=3) == 2
