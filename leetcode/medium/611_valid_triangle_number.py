"""
https://leetcode.com/problems/valid-triangle-number/
"""
import bisect


class Solution:
    @staticmethod
    def triangleNumber(nums: [int]) -> int:
        triangles = 0
        nums_length = len(nums)
        nums.sort()
        # print(nums)
        for i in range(nums_length):
            for j in range(i + 1, nums_length):
                k = bisect.bisect_left(nums, nums[i] + nums[j])
                if k > j:
                    triangles += (k - j - 1)
        # print(triangles)
        return triangles


assert Solution.triangleNumber(nums=[2, 2, 3, 4]) == 3
"""
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
"""
assert Solution.triangleNumber(nums=[4, 2, 3, 4]) == 4
